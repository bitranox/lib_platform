# -*- coding: utf-8 -*-
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

__title__ = 'lib_platform'
__name__ = 'lib_platform'
__version__ = '1.0.3'
