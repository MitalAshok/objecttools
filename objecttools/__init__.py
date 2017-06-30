"""Various tools for working with objects and classes in Python"""

from objecttools import cached_property, singletons

from objecttools.cached_property import *
from objecttools.singletons import *

__all__ = ['cached_property', 'singletons', 'cmp']

__all__.extend(cached_property.__all__)
__all__.extend(singletons.__all__)

__all__ = tuple(__all__)

__author__ = 'Mital Ashok'
__credits__ = ['Mital Ashok']
__license__ = 'MIT'
__version__ = '0.0.3'
__maintainer__ = 'Mital Ashok'
__author_email__ = __email__ = 'mital.vaja@googlemail.com'
__status__ = 'Development'

try:
    from __builtin__ import cmp
except ImportError:
    def cmp(x, y):
        """Return -1 if x < y, 0 if x == y, +1 if x > y."""
        if callable(getattr(x, '__cmp__', None)):
            cmp = x.__cmp__(y)
            if cmp is not NotImplemented:
                if cmp == 0:
                    return 0
                if cmp < 0:
                    return -1
                if cmp > 0:
                    return 1
        if callable(getattr(y, '__cmp__', None)):
            cmp = y.__cmp__(x)
            if cmp is not NotImplemented:
                if cmp == 0:
                    return 0
                if cmp < 0:
                    return 1
                if cmp > 0:
                    return -1
        return (x > y) - (x < y)
