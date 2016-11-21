# -*- coding: utf-8 -*-

"""
Copyright (C) 2016 IBM Corporation

Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

    Contributors:
        * Rafael Sene <rpsene@br.ibm.com>
        * Diego Fernandez-Merjildo <merjildo@br.ibm.com>
        * Roberto Oliveira <rdutra@br.ibm.com>
        """

import sys
import os
import time

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import controller

__all__ = []
#TODO: these values must be static
__version__ = '1.0.' + time.strftime("%Y%m%d%H%M%S")
__updated__ = time.strftime("%Y/%m/%d|%H:%M:%S")

class CLIError(Exception):
    ''' Command Line error class '''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

class FdprOptions(object):
    ''' Hold FDPR options '''
    opt_value = None
    warn_value = None
    verbose_value = None
    proc_value = None
    def __init__(self, opt, warn, verbose, proc):
        self.opt_value = opt
        self.warn_value = warn
        self.verbose_value = verbose
        self.proc_value = proc
    def get_opt(self):
        ''' Return opt option'''
        return self.opt_value
    def get_warn(self):
        ''' Return warn option'''
        return self.warn_value
    def get_verbose(self):
        ''' Return verbose option'''
        return self.verbose_value
    def get_proc(self):
        ''' Return processor option'''
        return self.proc_value

def main(argv=None):
    ''' SCA main function '''
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = '''
    --- Source Code Advisor (SCA) ---
    Report potential performance issues and possible remedies for a given
    executable.

    SCA will non-destructively instrument the executable and run the
    instrumented version, collecting performance data. Upon completion,
    a report will be presented listing any detected issues with possible
    remedies. '''

    program_license = '''%s

    Copyright (C) 2016 IBM Corporation

    Licensed under the Apache License, Version 2.0 (the “License”);
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
    either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

        Contributors:
            * Rafael Sene <rpsene@br.ibm.com>
            * Diego Fernandez-Merjildo <merjildo@br.ibm.com>
            * Roberto Oliveira <rdutra@br.ibm.com>
            ----------------------------------------------------------
            ''' % (program_shortdesc)

    try:
        parser = ArgumentParser(description=program_license,
                                formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-v", "--verbose", dest="verbose", type=int, choices=range(0, 4),
                            required=False, default=0,
                            help="set verbosity level [default: %(default)s]")
        parser.add_argument("-o", "--optimize", dest="opt", type=int, choices=range(1, 5),
                            required=False, default=3,
                            help="set optimization level [default: %(default)s]")
        parser.add_argument("-w", "--warning", dest="warn", type=int,
                            choices=range(1, 5), required=False, default=2,
                            help="set warning level [default: %(default)s]")
        parser.add_argument("-p", "--processor", dest="processor", type=str,
                            choices=['power7', 'power8'], required=False, default='power8',
                            help="set processor model [default: %(default)s]")
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument(dest="path",
                            help="path to the application binary [default: %(default)s]",
                            nargs='+')

        # Process arguments
        args, application_args = parser.parse_known_args()
        options_values = FdprOptions(args.opt, args.warn, args.verbose, args.processor)
        binary_path = args.path.pop(0)
        binary_args = ' ' + ' '.join(map(str, args.path))
        binary_args = binary_args + ' ' + ' '.join(map(str, application_args))

        #Run SCA
        controller.run_sca(binary_path, binary_args, options_values)

    except KeyboardInterrupt:
        return 0
    except Exception, excp:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(excp) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
