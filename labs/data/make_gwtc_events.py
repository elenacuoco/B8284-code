#!/usr/bin/env python3
"""
make_gwtc_events.py
===================
Rebuild ``gwtc_events.csv`` from the GWOSC event API.

Saves
-----
labs/data/gwtc_events.csv

One row per confident event. An event that appears in more than one catalogue
release is kept once, in its most recent release, so counting rows counts
events. The labs never run this script: they read the committed CSV and stay
offline. Run it when a new catalogue is published, commit the result and
update the count in ``README.md``.

    python labs/data/make_gwtc_events.py            # fetches from GWOSC
    python labs/data/make_gwtc_events.py all.csv    # reads a saved download
"""

import csv
import io
import os
import sys
import urllib.request

URL = "https://gwosc.org/eventapi/csv/allevents/"

# Confident releases only, oldest first: a later entry supersedes an earlier
# one for the same event. Marginal, preliminary, discovery-paper and external
# lists stay out, and so does GWTC-2, which GWTC-2.1 re-analysed: an event
# GWTC-2.1 demoted is not confident any more. A row here is an event the
# collaboration stands behind.
CONFIDENT = [
    "GWTC-1-confident",
    "GWTC-2.1-confident",
    "GWTC-3-confident",
    "GWTC-4.0",
    "GWTC-4.1",
    "GWTC-5.0",
]

COLUMNS = [
    "commonName", "catalog.shortName", "GPS",
    "mass_1_source", "mass_2_source", "total_mass_source",
    "chirp_mass_source", "final_mass_source",
    "total_mass_source_lower", "total_mass_source_upper",
    "chirp_mass_source_lower", "chirp_mass_source_upper",
    "luminosity_distance", "redshift",
    "chi_eff", "network_matched_filter_snr", "far", "p_astro",
]

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "gwtc_events.csv")


def main() -> int:
    if len(sys.argv) > 1:
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        with urllib.request.urlopen(URL, timeout=60) as r:
            text = r.read().decode("utf-8")

    rank = {name: k for k, name in enumerate(CONFIDENT)}
    best = {}
    for row in csv.DictReader(io.StringIO(text)):
        cat = row["catalog.shortName"]
        if cat not in rank:
            continue
        name = row["commonName"]
        if name not in best or rank[cat] >= rank[best[name]["catalog.shortName"]]:
            best[name] = row

    events = sorted(best.values(), key=lambda r: float(r["GPS"]))

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for row in events:
            w.writerow(row)

    per_cat = {}
    for r in events:
        per_cat[r["catalog.shortName"]] = per_cat.get(r["catalog.shortName"], 0) + 1
    print(f"wrote {os.path.basename(OUT)} — {len(events)} confident events")
    for cat in CONFIDENT:
        if cat in per_cat:
            print(f"  {cat:20} {per_cat[cat]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
