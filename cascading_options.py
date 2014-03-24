import argparse
import yaml


class cascading_parser(object):
    """
    Cascading options parser

    Allows program configuration via a cascading series of option sources
    the sources are read in the following order, with sources lower in the
    list overwriting those higher up.

    default: set via the add_option function, None if not specified
    config file: json or yaml, specified via the builtin '--config' or '-c' command line option
    command line: specified when calling the program
    """
    options = {}
    _cmdline = []

    def __init__(self, *args, **kwargs):
        # handle argparse options that are not supported
        for option in ['prefix_char', 'fromfile_prefix_chars', 'parents',
                       'conflict_handler']:
            if option in kwargs:
                raise Exception('{0} option not supported'.format(option))

        self._argparser = argparse.ArgumentParser(*args, **kwargs)
        self._argparser.add_argument('--config', '-c', metavar='file',
                                     help='config file location')
        self._parsed = False

    def add_option(self, *args, **kwargs):
        """
        Add option, passes positional and keyword arguments to argparse.add_arguments.
        Custom keyword argument is cmdline
          if cmdline=False then the option will be config file only
          if cmdline=True then the option will be command line only
        """
        if self._parsed:
            raise Exception('Cannot add additional arguments, they have already been parsed!')

        # handle reserved arguments
        for arg in args:
            if arg.replace('-', '') in ['config', 'c', 'help', 'h']:
                raise Exception('{0} is a reserved argument'.format(arg))
        argument = args[0].replace('-', '')

        # set default value in options
        if 'default' in kwargs:
            self.options[argument] = kwargs['default']
            kwargs['default'] = None
        else:
            self.options[argument] = None

        # if cmdline=False then it will be config file only
        # if cmdline=True then it will be command line only
        if 'cmdline' in kwargs:
            if kwargs['cmdline']:
                self._cmdline.append(argument)
                del kwargs['cmdline']
            else:
                return
        self._argparser.add_argument(*args, **kwargs)

    def cascade_options(self):
        """
        Parse config file and command line options and generate final settings.
        """
        if self._parsed:
            return
        self._parsed = True

        cmdline = self._argparser.parse_args()
        config = {}
        if cmdline.config:
            config = yaml.load(open(cmdline.config))
        # overload default values with config file
        for k, v in self.options.items():
            if k in config and k not in self._cmdline:
                self.options[k] = config[k]
            if hasattr(cmdline, k) and getattr(cmdline, k):
                self.options[k] = getattr(cmdline, k)
            setattr(self, k, self.options[k])

    def write_options(self, filename):
        """
        Write current settings to a YAML file.
        """
        tmp = self.options
        for k in self._cmdline:
            del tmp[k]
        with open(filename, 'w') as outfile:
            yaml.dump(tmp, outfile, indent=4, default_flow_style=True)

    # for drop-in argparse replacement
    add_argument = add_option

    def parse_args(self):
        self.cascade_options()
        return self
