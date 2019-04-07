# -*- coding: utf-8 -*-
import logging

try:
    from .lib_platform.lib_platform import *
except ImportError:
    logger = logging.getLogger()
    logger.debug('Import Error - this __init__.py is only meant for local package development')

__title__ = 'lib_platform'
__version__ = '1.0.0'
