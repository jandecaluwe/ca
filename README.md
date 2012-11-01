ca
==

Purpose
-------

Cellular automata simulator in Python.

I created this for two purposes. One is to get insight in cellular
automata. The second is to a reference model for hardware
implementations.

Installation
------------

If you prefer not to use `git clone`, just download the source code directory as a zip file.

After unzipping, make sure to rename the top-level directory to `ca`. This is because the code is implemented as a Python package, with `ca` as the top-level package name.

Usage
-----
At the top level in the `ca` directory, there are a number of games you can play using the Python interpreter. For example:

    python ca/fireworks.py

You can create your own games by subclassing the `generations` base class. See the existing games for examples.


Issues
------

Even though `Tkinter` is part of the standard Python library, you may have to install additional packages to make the gui work. This is because `Tkinter` is really an interface to `Tcl/Tk`, and these packages have to be installed also. On ubuntu, the following should work:

    sudo apt-get tcl-dev tk-dev python-tk


Author
------
Jan Decaluwe 2012

