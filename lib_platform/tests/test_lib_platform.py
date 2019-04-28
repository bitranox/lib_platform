"""lib_platform tests"""

import dill
from lib_platform.lib_platform import *
from lib_registry import *


def test_system_values():
    """
    >>> ### do not remove this line - marker doc basic usage start
    >>> import lib_platform

    >>> # get system as string
    >>> system = lib_platform.system

    >>> # bool is_platform_linux
    >>> is_platform_linux = lib_platform.is_platform_linux

    >>> # bool is_platform_darwin
    >>> is_platform_darwin = lib_platform.is_platform_darwin

    >>> # bool is_platform_posix
    >>> is_platform_posix = lib_platform.is_platform_posix        # either darwin or linux

    >>> # bool is_platform_windows
    >>> is_platform_windows = lib_platform.is_platform_posix      # also True for windows_xp or windows_wine

    >>> # bool is_platform_windows_xp
    >>> is_platform_windows_xp = lib_platform.is_platform_windows_xp

    >>> # bool is_platform_windows_wine
    >>> is_platform_windows_wine = lib_platform.is_platform_windows_wine

    >>> # bool is_platform_windows_wine_xp
    >>> is_platform_windows_wine_xp = lib_platform.is_platform_windows_wine_xp

    >>> # string username lib_platform.username
    >>> username = lib_platform.username

    >>> # string fqdn hostname
    >>> hostname = lib_platform.hostname

    >>> # string hostname short
    >>> hostname_short = lib_platform.hostname_short

    >>> # bool is_python2
    >>> is_python2 = lib_platform.is_python2

    >>> # bool is_python3
    >>> is_python3 = lib_platform.is_python3

    >>> # path to userhome
    >>> path_userhome = lib_platform.path_userhome
    >>> ### do not remove this line - marker doc basic usage end

    """

    if is_platform_linux:
        assert system == 'linux'
        assert is_platform_posix
        assert not is_platform_darwin
        assert not is_platform_windows
        assert not is_platform_windows_wine
        assert not is_platform_windows_xp
    if is_platform_darwin:
        assert system == 'darwin'
        assert is_platform_posix
        assert not is_platform_linux
        assert not is_platform_windows
        assert not is_platform_windows_wine
        assert not is_platform_windows_xp

    if is_platform_posix:
        assert system == 'darwin' or system == 'linux'
        assert is_platform_darwin or is_platform_linux
        assert not is_platform_windows
        assert not is_platform_windows_wine
        assert not is_platform_windows_xp

    if is_platform_windows:
        windows_flavours = ['windows', 'windows_wine', 'windows_xp', 'windows_wine_xp']
        assert system in windows_flavours
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix

    if is_platform_windows_wine:
        assert system == 'windows_wine' or 'windows_wine_xp'
        assert is_platform_windows
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix

    if is_platform_windows_xp:
        assert system == 'windows_xp' or 'windows_wine_xp'
        assert is_platform_windows
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix

    if is_platform_windows_xp and is_platform_windows_wine:
        assert system == 'windows_wine_xp'
        assert is_platform_windows
        assert is_platform_windows_xp
        assert is_platform_windows_wine
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix

    if is_platform_windows and not is_platform_windows_wine and not is_platform_windows_xp:
        assert system == 'windows'
        assert is_platform_windows
        assert not is_platform_windows_xp
        assert not is_platform_windows_wine
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix


def test_function_to_pickle():
    if is_platform_windows:
        print('windows')
    if get_system() == 'windows':
        print('windows')


def test_if_pickable():
    pickled_object = dill.dumps(test_function_to_pickle)
    unpickled_object = dill.loads(pickled_object)


def test_fake_xp_function():
    return 'xp'


def test_fake_xp():
    if is_platform_windows and not is_platform_windows_wine:
        save_platform_release_function = platform.release
        platform.release = test_fake_xp_function
        assert get_is_platform_windows_xp() is True
        assert get_system() == 'windows_xp'
        assert is_platform_windows
        assert not is_platform_windows_wine
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix
        platform.release = save_platform_release_function
