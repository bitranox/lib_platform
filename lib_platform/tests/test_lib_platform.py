"""lib_platform tests"""

import dill
from lib_platform import *
from lib_platform.lib_platform import *
from lib_registry import *


def test_system_values():
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
        windows_flavours = ['windows', 'windows_wine', 'windows_xp']
        assert system in windows_flavours
        assert not is_platform_linux
        assert not is_platform_darwin
        assert not is_platform_posix

    if is_platform_windows_wine:
        assert system == 'windows_wine'
        assert is_platform_windows
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


def test_fake_xp():
    if is_platform_windows and not is_platform_windows_wine:
        save_current_release_function = platform.release
        platform.release = fake_release_function_xp
        assert lib_platform.get_system() == 'windows_xp'
        assert get_is_platform_windows_xp() is True
        platform.release = save_current_release_function
        assert lib_platform.get_system() == 'windows'
        assert get_is_platform_windows_xp() is False


def fake_release_function_xp():
    return 'xp'
