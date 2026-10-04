# Getting started (for students)

This page is the checklist version of the [README](README.md): what to click,
in what order, and what to do once a notebook is open.

## 1. Open the course

Go to the repository on GitHub, click the green **Code** button, open the
**Codespaces** tab, then **Create codespace on main**. Do not clone the repo
to your laptop unless you have a specific reason to — the codespace already
has everything installed.

The first build takes a few minutes: GitHub is reading
`.devcontainer/devcontainer.json` and installing `requirements.txt` for you.
Every later codespace you open on this repository starts in seconds.

You do not need to run `pip install`, create a virtual environment, or install
Jupyter yourself. If a notebook asks you to install something, that is a bug —
report it, don't work around it.

## 2. Find your seat: the two index pages

The course is two parts, each with its own index:

- [`python/index.md`](python/index.md) — the Python primer, sessions P1 to P4
- `labs/index.md` — the laboratories, H01 to H13, which appear as they are
  released

Start at Part 1 if you have never programmed, or have only used Python a
little. If you already write Python comfortably, `python/index.md` tells you
exactly which parts of the primer to skim and which to still read in full —
read that page's "If you already know Python" section before skipping ahead.

## 3. Work through a notebook

Each notebook is meant to be run, not read. For every notebook:

1. Open the notebook and run the cells from the top, in order.
2. Where the notebook poses a task, write your answer in the cell left for
   it. Laboratories H01 to H05 show a worked answer under the question, closed,
   so you can check your tools; from H06 on, nothing is printed for you — you
   check your own answer against what the task asks you to find.
3. Change the parameters at the top of the notebook (they are called out for
   this reason) and re-run. Watching something break, and working out why,
   is part of the work, not a detour from it.
4. Read the `## Software` section at the end before moving on — it names the
   packages the notebook used and how to cite them.

Move to the next notebook only once the current one's cells all run without
errors and its tasks are answered.

## 4. What "done" looks like for a notebook

- Every cell has been run (no cell left with an old, stale, or missing
  output).
- Every task cell has your answer in it, not a placeholder.
- You changed at least one parameter at the top of the notebook and saw what
  it did.

## Ground rules

- **Everything runs offline.** The data used by Part 2 is already committed
  in `labs/data/`. No cell needs the internet once the codespace has built. If
  something fails because it can't reach a server, that's a bug — report it,
  don't try to fetch the data yourself.
- **The codespace has a free quota.** 120 core-hours per month per account
  (about 60 hours on the default 2-core machine), or 180 core-hours per month
  if you're verified through [GitHub Education](https://github.com/education).
  Stop your codespace when you're not using it (it doesn't stop on its own
  just because your laptop is closed) — the Codespaces tab on GitHub lists
  your running ones.
- **If you'd rather work locally:** clone the repository, use Python 3.10 to
  3.13, `pip install -r requirements.txt` in a virtual environment, then open
  the notebooks with Jupyter or VS Code. The notebooks behave identically
  either way.

## If something doesn't work

Check first whether the notebook itself tells you what's expected — every
notebook states the physics it needs before it asks for code. If a cell errors
out on a fresh, unmodified run, or the codespace fails to build, that's a bug
in the course, not something to debug on your own: report it to your
instructor with the notebook name and the error message.
