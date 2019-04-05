# -*- coding: utf-8 -*-

# this is only for local development when the package is actually not installed
try:
    from .lib_platform.lib_platform import *
except ImportError:
    pass

__title__ = 'lib_platform'
__version__ = '1.0.0'
