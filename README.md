# B8284 — Python for Gravitational Waves

A course that starts from no programming at all and ends at real gravitational
wave data analysis: matched filtering on the strain recorded on 14 September
2015, Bayesian parameter estimation, a neural network measured against the
filter, an un-modelled search, and the catalogue of everything the detectors
have found.

Everything is a Jupyter notebook. Everything runs offline — the data is cached
and committed with the course, so no cell depends on a network connection.

**The notebooks are published as the course goes on.** What is here is what
has been released so far: the tables below list it.

## Open it

Click **Code → Create codespace on main** on this repository (or the green
"Code" button, then the "Codespaces" tab). GitHub builds an environment from
`.devcontainer/devcontainer.json` and installs everything in `requirements.txt`
automatically — the first build takes a few minutes, later ones are faster.
Once it opens, the notebooks run exactly as they do locally: no `conda`, no
`pip install` by hand.

Free quota: 120 core-hours per month per account (about 60 hours on the default
2-core machine), 180 core-hours per month for verified students and teachers
via [GitHub Education](https://github.com/education).

To run it on your own machine instead: clone the repository, make a virtual
environment with Python 3.10 to 3.13, `pip install -r requirements.txt`, and
open the notebooks with Jupyter or VS Code.

New to the course? [`GETTING_STARTED.md`](GETTING_STARTED.md) is the
step-by-step checklist: what to click, where to start, and what "done" looks
like for a notebook.

## The demo

[`demo/gw150914_first_look.ipynb`](demo/gw150914_first_look.ipynb) is the
notebook shown in the first class: 32 seconds of real LIGO strain, the signal
invisible in it, the same seconds whitened until the chirp comes out of both
detectors, and the time–frequency picture. It runs in about a minute, needs
nothing but this repository, and assumes no Python at all — it is there to be
watched before it is understood. Everything in it is done properly, and by
you, in the laboratories.

## The course

**The Python primer** ([`python/`](python/index.md)): 5 sessions,
P1 to P5, assuming nothing.

| Session | Notebook |
|---|---|
| `P1` | [`python/P1_getting_started.ipynb`](python/P1_getting_started.ipynb) |
| `P2` | [`python/P2_control_flow_functions.ipynb`](python/P2_control_flow_functions.ipynb) |
| `P3` | [`python/P3_data_structures_numpy.ipynb`](python/P3_data_structures_numpy.ipynb) |
| `P4` | [`python/P4_scientific_stack.ipynb`](python/P4_scientific_stack.ipynb) |
| `P5` | [`python/P5_code_you_can_trust.ipynb`](python/P5_code_you_can_trust.ipynb) |

**The laboratories** ([`labs/`](labs/index.md)), published on the day
they are taught. The names are the course's own, H01 to H10.

| Laboratory | Notebook |
|---|---|
| `H01` | [`labs/H01_first_waveform.ipynb`](labs/H01_first_waveform.ipynb) — Your first waveform |
| `H02` | [`labs/H02_linear_systems.ipynb`](labs/H02_linear_systems.ipynb) — Linear systems: the oscillator a detector is made of |
| `H03` | [`labs/H03_time_series.ipynb`](labs/H03_time_series.ipynb) — Time series: lecture 9 in examples |
| `H03` | [`labs/H03_homework_mirror_noise.ipynb`](labs/H03_homework_mirror_noise.ipynb) — Homework: the noise of a mirror on a spring |
| `H04` | [`labs/H04_class_real_noise.ipynb`](labs/H04_class_real_noise.ipynb) — In class: the real noise of Virgo |
| `H04` | [`labs/H04_home_gwosc_data.ipynb`](labs/H04_home_gwosc_data.ipynb) — At home: LIGO data from GWOSC |
| `H05` | [`labs/H05_class_signal_processing.ipynb`](labs/H05_class_signal_processing.ipynb) — In class: signal processing on real data |
| `H05` | [`labs/H05_home_signal_processing.ipynb`](labs/H05_home_signal_processing.ipynb) — At home: filters and the time–frequency plane |
| `H06` | [`labs/H06_matched_filter.ipynb`](labs/H06_matched_filter.ipynb) — The matched filter on real data and simulated glitches |
| `H07` | [`labs/H07_psd_and_whitening.ipynb`](labs/H07_psd_and_whitening.ipynb) — The PSD and whitening: a practical session |
| `H08` | [`labs/H08_parameter_estimation.ipynb`](labs/H08_parameter_estimation.ipynb) — Parameter estimation: statistical error and instrumental effects |
| `H09` | [`labs/H09_gwtc_population.ipynb`](labs/H09_gwtc_population.ipynb) — The catalog as a population of events |
| `H10` | [`labs/H10_cnn_chirp_detection.ipynb`](labs/H10_cnn_chirp_detection.ipynb) — A convolutional network and the matched filter compared |

**Your own notebook**: [`sandbox.ipynb`](sandbox.ipynb). Nothing in the
course reads it. Try things there before they go into an answer.

## Conventions

The notebooks are plain Jupyter markdown: no build step, no static site, no
extra extensions. Boxed asides are written as indented quotations, equations as
LaTeX between `$` or `$$`, and references as ordinary text at the point where
they are used.

Every formula names its symbols where it first appears. The notebooks read
their data from `labs/data/` and the demo from `demo/data/`. Every laboratory
ends by saying which packages it used.
