# STDLIB
import os

# PROJECT
from .lib_platform import *


# Python 2.7 Version
def get_version():   # type: ignore
    with open(os.path.join(os.path.dirname(__file__), 'version.txt'), mode='r') as version_file:
        version = version_file.readline()
    return version


__title__ = 'lib_platform'
__name__ = 'lib_platform'
__version__ = get_version()  # type: ignore
