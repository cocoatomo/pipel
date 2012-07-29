from pip.commands import search

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


class ListCommand(search.SearchCommand):
    name = 'list'
    usage = '%prog package_name'
    summary = 'list package'

    def search(self, query, index_url):
        pypi = xmlrpclib.ServerProxy(index_url, pip.download.xmlrpclib_transport)
        hits = pypi.search({'name': query})
        return hits

ListCommand()
