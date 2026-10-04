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

**The Python primer** ([`python/`](python/index.md)): four sessions,
P1 to P4, assuming nothing.

| Session | Notebook |
|---|---|
| `P1` | [`python/P1_getting_started.ipynb`](python/P1_getting_started.ipynb) |
| `P2` | [`python/P2_control_flow_functions.ipynb`](python/P2_control_flow_functions.ipynb) |
| `P3` | [`python/P3_data_structures_numpy.ipynb`](python/P3_data_structures_numpy.ipynb) |
| `P4` | [`python/P4_scientific_stack.ipynb`](python/P4_scientific_stack.ipynb) |

**The laboratories**, H02 to H11, are published here on the day they
are taught. None is out yet.

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
