# Part 1 — The Python primer (Lessons 1 to 4)

Four lessons, about eight hours, starting from nothing. No prior programming is
assumed.

The aim is narrow and practical: to reach the point where the rest of the
course is about gravitational waves rather than about Python. This is not a
software engineering course and it is not a Python course for its own sake.
Every example here is one you meet again later, which is why you will be
plotting a chirp before you have written a `for` loop over a list of names.

## The four lessons

| Lesson | Notebook | Covers |
|---|---|---|
| 1 | [`P1_getting_started.ipynb`](P1_getting_started.ipynb) | What Python is and what is running; variables, types, conversion, operators; reading an error message; your first plot |
| 2 | [`P2_control_flow_functions.ipynb`](P2_control_flow_functions.ipynb) | Booleans and logic; `if`/`elif`/`else`; `for` and `while`, `break` and `continue`; functions, parameters, defaults, scope, docstrings; `try`/`except` |
| 3 | [`P3_data_structures_numpy.ipynb`](P3_data_structures_numpy.ipynb) | Lists and their methods, tuples, sets, dictionaries, nesting; then NumPy arrays, slicing, masks, **vectorised thinking** |
| 4 | [`P4_scientific_stack.ipynb`](P4_scientific_stack.ipynb) | Text, CSV and JSON files; modules, imports and `pip`; HDF5 and frame files; Matplotlib, SciPy and pandas; a real strain file opened and plotted |

**How these lessons work.** There is no blackboard in the primer. Every example
is a cell, and every cell is meant to be run — read the sentence, run the cell,
look at what came out, then change something in it and run it again. The cells
are deliberately short, a dozen lines at most, so that each one can be taken
apart on its own.

**What eight hours can and cannot do.** Eight hours will not turn someone who
has never programmed into someone who writes analysis code from an empty cell.
They will take you to where you can **read, run, modify and debug a notebook
somebody else structured**, which is what every lesson in Part 2 asks of you.
Getting further than that is a matter of the hours you spend between lessons,
which is why each lesson ends with work to do before the next.

Lesson 4 ends by opening the real strain data recorded on 14 September 2015 —
from a file on the disk, with no network involved — and plotting it. It does
not analyse it: recovering a signal needs a model of the noise and a model of
the signal, and those are built in Part 2. Lesson 11 is where that work starts.

## If you already know Python

Skim Lessons 1 to 3, then do Lesson 4 in full: the HDF5 material is specific to
gravitational wave data and worth reading even if the rest is familiar. The one
habit worth checking you have is **vectorised thinking** — a Python loop over
4096 samples per second of strain data will be the slowest thing you write, and
NumPy makes it unnecessary. If that sentence is already obvious to you, go
straight to [Part 2](../labs/index.md).
