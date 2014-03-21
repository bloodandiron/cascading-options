=========================
Cascading Argument Parser
=========================

Allows program configuration via a cascading series of option sources
the sources are read in the following order, with sources lower in the
list overwriting those higher up.

    * default: set via the add_option function, None if not specified
    * config file: json or yaml, specified via the builtin '--config' or '-c' command line option
    * command line: specified when calling the program

Usage
~~~~~
Acts as a semi drop-in replacement to the standard argparse module.

For commandline only options use::

    cascading_parser.add_option(..., cmdline=True)

For config file only options use::

    cascading_parser.add_option(..., cmdline=False)

Default behavior is to have the option avaliable in both.
