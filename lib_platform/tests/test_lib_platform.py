"""lib_platform tests"""

import dill
from lib_platform import *
from lib_platform.lib_platform import *
from lib_registry import *


def test_wine_support():
    if is_platform_windows:
        assert not is_platform_windows_wine

        """
        # todo: we need admin rights to do that in travis

        create_wine_registry_entry()
        is_wine = get_is_platform_windows_wine()
        assert is_wine
        delete_wine_registry_entry()

        def create_wine_registry_entry():
            # stub
            pass

        def delete_wine_registry_entry():
            # stub
            pass
        """


def test_function_to_pickle():
    if is_platform_windows:
        print('windows')
    if get_system() == 'windows':
        print('windows')


def test_if_pickable():
    pickled_object = dill.dumps(test_function_to_pickle)
    unpickled_object = dill.loads(pickled_object)


def test_fake_xp():
    if is_platform_windows:
        save_current_release_function = platform.release
        platform.release = fake_release_function_xp
        assert lib_platform.get_system() == 'windows_xp'
        assert get_is_platform_windows_xp() is True
        platform.release = save_current_release_function
        assert lib_platform.get_system() == 'windows'
        assert get_is_platform_windows_xp() is False


def fake_release_function_xp():
    return 'xp'
