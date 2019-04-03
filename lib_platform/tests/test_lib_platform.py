"""lib_platform tests"""

import dill
import lib_platform
from lib_platform import *
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


def my_function_pickle_test():
    if is_platform_windows:
        print('windows')
    if get_system() == 'windows':
        print('windows')


def test_if_pickable():
    pickled_object = dill.dumps(my_function_pickle_test)
    unpickled_object = dill.loads(pickled_object)
