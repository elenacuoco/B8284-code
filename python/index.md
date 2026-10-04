# Python Primer

Four sessions — eight hours — starting from nothing. No prior programming is
assumed.

The aim is narrow and practical: get you to the point where the labs are about
gravitational waves rather than about Python. We are not teaching software
engineering and we are not teaching Python for its own sake. Every example here
is one you will meet again later in the course, which is why you will be
plotting a chirp before you have written a `for` loop over a list of names.

## The four sessions

| Notebook | Covers | Reference modules |
|---|---|---|
| [`P1_getting_started.ipynb`](P1_getting_started.ipynb) | What Python is and what is running; variables, types, conversion, operators; reading an error message; your first plot | 1 |
| [`P2_control_flow_functions.ipynb`](P2_control_flow_functions.ipynb) | Booleans and logic; `if`/`elif`/`else`; `for` and `while`, `break` and `continue`; functions, parameters, defaults, scope, docstrings; `try`/`except` | 2, 3 |
| [`P3_data_structures_numpy.ipynb`](P3_data_structures_numpy.ipynb) | Lists and their methods, tuples, sets, dictionaries, nesting; then NumPy arrays, slicing, masks, **vectorised thinking** | 4 |
| [`P4_scientific_stack.ipynb`](P4_scientific_stack.ipynb) | Text, CSV and JSON files; modules, imports and `pip`; HDF5 and frame files; Matplotlib, SciPy and pandas; a real strain file opened and plotted | 5 |

Each session condenses the modules named in the last column, which are in
`reference/` with their examples and exercises. The sessions are where the
material is taught with gravitational wave data as the setting; the modules are
where the same ideas are drilled at length.

They run **one a week, alongside the first lectures**, so that each session has
a week of practice behind it before the next one arrives. The dates are in the
teaching schedule; these pages sit together at the end of the notes because
that is where they are easiest to come back to.

The fourth session ends by opening the real strain data from 14 September 2015
— from a file on the disk, with no network involved — and plotting it. It does
not analyse it: recovering a signal needs a model of the noise and a model of
the signal, which are Parts V and VI. That work belongs to the laboratories and
`H07` is where it happens.

> **How these sessions run**
>
> There is no blackboard in the Python sessions. Every example is a cell that is
> projected and **run in front of you**, one at a time. You are expected to have
> the same notebook open and to run it as we go.
>
> The cells are deliberately short — a dozen lines at most — and narrow enough
> to be read from the back of the room. Where an idea needs more than that, it is
> split across two cells with a sentence between them, so that the output of the
> first is on the screen while the second is explained.

> **Careful — What eight hours can and cannot do**
>
> Eight hours will not turn someone who has never programmed into someone who
> writes analysis code from an empty cell. It will take you to where you can
> **read, run, modify and debug a notebook somebody else structured**, which is
> what every laboratory in this course actually asks of you.
>
> Getting further than that is a matter of the hours you spend between sessions,
> which is why each one ends with work to do before the next.

## Self-study reference

`reference/` holds the examples and exercises of the five modules the
sessions are condensed from, with solutions beside them. Use it if
you are new to Python or as a lookup when something in a lab does not behave.

| Module | Topic |
|---|---|
| 1 | Getting started — variables, types, input/output, operators |
| 2 | Control flow — booleans, `if`/`elif`/`else`, loops, `break`/`continue` |
| 3 | Functions and error handling — parameters, scope, docstrings, `try`/`except` |
| 4 | Data structures — lists, tuples, sets, dictionaries, nesting |
| 5 | Files and libraries — text, CSV and JSON files; modules and imports |

## If you already know Python

Skim `P1`–`P3` and do `P4` in full, for the HDF5 and frame files. The
one habit worth checking you have is **vectorised thinking** — a Python loop
over 4096 samples per second of strain data will be the slowest thing in your
project and NumPy makes it unnecessary. If that sentence is already obvious to
you, go straight to the labs.
