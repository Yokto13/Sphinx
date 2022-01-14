# Documentation for fellow coders
Hello!
If you're reading this you probably want to contribute to the project
(or something broke and you're trying to figure out how this dammed thing works xD).

The majority of things are documented in the code itself so here I'm going to give mostly an
overview of the structure.

## models
The Sphinx works with two types of objects and those are **Statistics** and **Questions**.
They have corresponding abstract classes that define some basic properties they ought to have.
Those objects are mostly boxes that carry some data and shouldn't be hard to understand.
All classes defining questions are stored in *questions.py* and classes for statistics in
*statistics.py*.

One thing to note is the *StatisticsHolder* that manages statistics.
It might be tempting to hardcode all statistics to a question as it's properties but the holder
provides convenient methods to handle all objects that inherit from the *AbstractStatistics*
at once.
This will come in handy when more than *ScoreStatistics* is needed.

## ui
*ui* provides basic functionality for working with data.

## tui
This folder contains anything that builds on top of the Text User Interface.

### multiline_label.py
This class uses a series of labels placed in rows to display text across multiple rows.


## main_tui.py
This file contains the definition of the TUI and also the main logic that handles
answering, loading, and showing questions/answers and statistics.
If you are not familiar with picotui I highly recommend trying first examples in its 
[repo](https://github.com/pfalcon/picotui).

A lot of the displayd objects calls some methods *on changed* those methods always have the 
followin signature:
```
def name_of_the_object_changed(w):
```
