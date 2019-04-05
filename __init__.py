# -*- coding: utf-8 -*-

# this is only for local development when the package is actually not installed
# noinspection PyBroadException
try:
    from .lib_platform.lib_platform import *
except Exception:
    pass

__title__ = 'lib_platform'
__version__ = '1.0.0'
