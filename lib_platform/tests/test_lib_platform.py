"""lib_platform tests"""

from lib_platform import *
from lib_registry import *


def test_wine_support():
    if is_platform_windows:
        assert not is_platform_windows_wine
        # create_wine_registry_entry()
        # is_wine = get_is_platform_windows_wine()
        # assert is_wine
        # delete_wine_registry_entry()


def create_wine_registry_entry():
    pass


def delete_wine_registry_entry():
    pass
