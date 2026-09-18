# B8284 — Python for Gravitational Waves

A course that starts from no programming at all and ends at real gravitational
wave data analysis: matched filtering on the strain recorded on 14 September
2015, Bayesian parameter estimation, a neural network measured against the
filter, an un-modelled search, and the catalogue of everything the detectors
have found.

Everything is a Jupyter notebook. Everything runs offline — the data is cached
and committed with the course, so no cell depends on a network connection.

**The lessons are published as the course goes on.** What is here is what has
been released; the table below says what is still to come.

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
like for a lesson.

## The course

**Part 1 — the Python primer** ([`python/`](python/index.md)). Four lessons,
about eight hours, assuming nothing. The aim is to reach the point where the
rest of the course is about gravitational waves rather than about Python.

| Lesson | Notebook | What it covers |
|---|---|---|
| 1 | `python/P1_getting_started.ipynb` | The notebook and the kernel; variables, types and conversion; reading an error message; your first plot |
| 2 | `python/P2_control_flow_functions.ipynb` | Booleans and logic; `if`/`elif`/`else`; `for` and `while`; functions, defaults, scope, docstrings; `try`/`except` |
| 3 | `python/P3_data_structures_numpy.ipynb` | Lists, tuples, sets and dictionaries; NumPy arrays, slicing, boolean masks and vectorised thinking |
| 4 | `python/P4_scientific_stack.ipynb` | Text, CSV, JSON and HDF5 files; modules and imports; NumPy, SciPy, pandas and Matplotlib; a real strain file opened and plotted |

**Part 2 — gravitational wave analysis** (`labs/`, published lesson by lesson
as the course goes on). Eleven hands-on lessons, from the geodesic equation to
the event catalogue. Each one states the physics it needs, poses its tasks, and
leaves you the cell to answer them in.

| Lesson | Notebook | What you build |
|---|---|---|
| 5 | `labs/H02_geodesics.ipynb` | A geodesic integrator in Schwarzschild: Mercury's perihelion shift and the binary pulsar's, from one equation |
| 6 | `labs/H03_first_waveform.ipynb` | The Newtonian chirp, from the quadrupole formula to a waveform — and the chirp mass recovered back out of it |
| 7 | `labs/H04_source_landscape.ipynb` | Every class of source on the characteristic-strain plane, against the detector curves |
| 8 | `labs/H05_noise_budget.ipynb` | A sensitivity curve assembled from five noise terms, and the inspiral range it implies |
| 9 | `labs/H06_psd_and_whitening.ipynb` | Power spectral density estimation, whitening, instrumental lines — and the first sight of GW150914 |
| 10 | `labs/H07_timefreq_gw150914.ipynb` | The time–frequency plane: a Q-scan of the first detection, and a mass read off the track |
| 11 | `labs/H08_matched_filter.ipynb` | Matched filtering on real data, and the glitches, scattered light and wandering lines it was not designed for |
| 12 | `labs/H09_parameter_estimation.ipynb` | A Bayesian posterior you can see: the distance–inclination degeneracy and the three instrumental effects that move the answer |
| 13 | `labs/H10_cnn_chirp_detection.ipynb` | A convolutional network against your own matched filter, at the same false alarm rate |
| 14 | `labs/H11_gwtc_population.ipynb` | The catalogue as a population: the mass plane, the chirp mass, and the selection effect underneath both |
| 15 | `labs/H12_wdf_search.ipynb` | A search with no template: the Wavelet Detection Filter on GW150914, against the matched filter that knew the shape |

Work through them in that order. The notebook file names keep their original
numbering, so the lesson number and the file number do not match; the tables
above and the two index pages are the order to follow.

## Conventions

The notebooks are plain Jupyter markdown: no build step, no static site, no
extra extensions. Boxed asides are written as indented quotations, equations as
LaTeX between `$` or `$$`, and references as ordinary text at the point where
they are used.

Every formula names its symbols where it first appears. Every lesson that reads
data reads it from `labs/data/`. Every lesson ends by saying which packages it
used.
