# STDLIB
import os

# PROJECT
from .lib_platform import system
from .lib_platform import is_platform_linux
from .lib_platform import is_platform_darwin
from .lib_platform import is_platform_posix
from .lib_platform import is_platform_windows
from .lib_platform import is_platform_windows_xp
from .lib_platform import is_platform_windows_wine
from .lib_platform import is_platform_windows_wine_xp
from .lib_platform import username
from .lib_platform import hostname
from .lib_platform import hostname_short
from .lib_platform import is_python2
from .lib_platform import is_python3
from .lib_platform import path_userhome
from .lib_platform import get_system                        # this we need for pytest
from .lib_platform import get_is_platform_windows_xp        # this we need for pytest
from .lib_platform import is_user_admin

# Python 2.7 Version
def get_version():   # type: ignore
    with open(os.path.join(os.path.dirname(__file__), 'version.txt'), mode='r') as version_file:
        version = version_file.readline()
    return version


__title__ = 'lib_platform'
__name__ = 'lib_platform'
__version__ = get_version()  # type: ignore
