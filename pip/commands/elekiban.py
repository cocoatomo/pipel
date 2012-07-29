import sys
import textwrap
import pkg_resources
import pip.download
from pip.basecommand import Command, SUCCESS
from pip.util import get_terminal_size
from pip.log import logger
from pip.backwardcompat import xmlrpclib, reduce, cmp
from pip.exceptions import CommandError
from pip.status_codes import NO_MATCHES_FOUND
from distutils.version import StrictVersion, LooseVersion


class ElekibanCommand(Command):
    name = 'elekiban'
    usage = '%prog'
    summary = 'joke command'

    def run(self, options, args):
        print('Shimura!?')

ElekibanCommand()
