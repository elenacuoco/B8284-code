# Python Primer

Four sessions and two extras, starting from nothing. No prior programming
is assumed.

The aim is narrow and practical: get you to the point where you can read, run
and change a notebook that somebody else wrote. We are not teaching software
engineering and we are not teaching Python for its own sake. The examples are
the plainest ones: the marks of a class, the temperature through a day and a
tone under a hiss that you can hear. Numbers that are not plain examples are
said to be made up. The last session, P4, opens the course's own
data.


## The sessions

| Notebook | Covers | Reference modules |
|---|---|---|
| [`P1_getting_started.ipynb`](P1_getting_started.ipynb) | What Python is and what is running; variables, types, conversion, operators; reading an error message; your first plot | 1 |
| [`P2_control_flow_functions.ipynb`](P2_control_flow_functions.ipynb) | Booleans and logic; `if`/`elif`/`else`; `for` and `while`, `break` and `continue`; functions, parameters, defaults, scope, docstrings; `try`/`except`; the marks of a class and a sum of money that doubles | 2, 3 |
| [`P3_data_structures_numpy.ipynb`](P3_data_structures_numpy.ipynb) | Lists and dictionaries, with the arms of the detectors; tuples and sets; NumPy arrays, a day of temperatures, the loop against the array, slicing, masks, **vectorised thinking**; labelled plots; a tone under noise | 4 |
| [`P4_scientific_stack.ipynb`](P4_scientific_stack.ipynb) | Text and CSV files with pandas; JSON; HDF5; SciPy and a straight line through points; modules and imports; the course's strain file and catalogue of events; restart and run all and `assert`; git, the minimum | 5 |

Two more notebooks are extras, for anyone who wants to go further: [`P5_code_you_can_trust.ipynb`](P5_code_you_can_trust.ipynb) (names, constants, small functions and `assert` checks; git; a module, then a package with a test) and [`P6_primer_on_the_course_data.ipynb`](P6_primer_on_the_course_data.ipynb) (the same Python on the numbers of the course, with a small module). What they teach is in P3 and P4 in short form.

Each session condenses the modules named in the last column, which are in
`reference/` with their examples and exercises. The modules are where the same
ideas are drilled at length.

They are taught **in order**, each one building on the practice done after the
one before. These pages sit together at the end of the notes because that is
where they are easiest to come back to.

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

> **Careful — What the primer can and cannot do**
>
> A primer will not turn someone who has never programmed into someone who
> writes analysis code from an empty cell. It will take you to where you can
> **read, run, modify and debug a notebook somebody else structured**.
>
> Getting further than that is a matter of the hours you spend between sessions,
> which is why each one ends with work to do before the next.

## Self-study reference

`reference/` holds the examples and exercises of the five modules the
sessions are condensed from, with solutions beside them. Use it if
you are new to Python or as a lookup when something does not behave.

| Module | Topic |
|---|---|
| 1 | Getting started — variables, types, input/output, operators |
| 2 | Control flow — booleans, `if`/`elif`/`else`, loops, `break`/`continue` |
| 3 | Functions and error handling — parameters, scope, docstrings, `try`/`except` |
| 4 | Data structures — lists, tuples, sets, dictionaries, nesting |
| 5 | Files and libraries — text, CSV and JSON files; modules and imports |

## If you already know Python

Skim `P1`–`P3` and do `P4` in full, for HDF5 and the course's data. The one
habit worth checking you have is **vectorised thinking**. A Python loop over a
long series of numbers will be the slowest thing in your project and NumPy
makes it unnecessary. If that sentence is already obvious to you, start
at `P4`.
