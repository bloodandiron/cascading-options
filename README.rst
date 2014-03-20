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

Use cascading_parser.cascading_parser(..., config_required=True) to force the config option as required (default: False).
Use cascading_parser.add_option(..., cmdline=True) to have an option only avaliable on the command line and cmdline=False to have it only avaliable in the config file (default: Avaliable in both)