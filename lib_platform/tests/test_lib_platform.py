"""lib_platform tests"""

# STDLIB
import platform

# DEPS
import dill                                 # type: ignore

# OWN
try:
    from . import lib_platform              # type: ignore
except ImportError:
    import lib_platform                     # type: ignore


def test_system_values():
    # type: () -> None
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

    >>> # is user administrator (has user admin rights)
    >>> is_user_admin = lib_platform.is_user_admin
    >>> ### do not remove this line - marker doc basic usage end

    """

    if lib_platform.is_platform_linux:
        assert lib_platform.system == 'linux'
        assert lib_platform.is_platform_posix
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_windows
        assert not lib_platform.is_platform_windows_wine
        assert not lib_platform.is_platform_windows_xp
    if lib_platform.is_platform_darwin:
        assert lib_platform.system == 'darwin'
        assert lib_platform.is_platform_posix
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_windows
        assert not lib_platform.is_platform_windows_wine
        assert not lib_platform.is_platform_windows_xp

    if lib_platform.is_platform_posix:
        assert lib_platform.system == 'darwin' or lib_platform.system == 'linux'
        assert lib_platform.is_platform_darwin or lib_platform.is_platform_linux
        assert not lib_platform.is_platform_windows
        assert not lib_platform.is_platform_windows_wine
        assert not lib_platform.is_platform_windows_xp

    if lib_platform.is_platform_windows:
        windows_flavours = ['windows', 'windows_wine', 'windows_xp', 'windows_wine_xp']
        assert lib_platform.system in windows_flavours
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_posix

    if lib_platform.is_platform_windows_wine:
        assert lib_platform.system == 'windows_wine' or 'windows_wine_xp'
        assert lib_platform.is_platform_windows
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_posix

    if lib_platform.is_platform_windows_xp:
        assert lib_platform.system == 'windows_xp' or 'windows_wine_xp'
        assert lib_platform.is_platform_windows
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_posix

    if lib_platform.is_platform_windows_xp and lib_platform.is_platform_windows_wine:
        assert lib_platform.system == 'windows_wine_xp'
        assert lib_platform.is_platform_windows
        assert lib_platform.is_platform_windows_xp
        assert lib_platform.is_platform_windows_wine
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_posix

    if lib_platform.is_platform_windows and not lib_platform.is_platform_windows_wine and not lib_platform.is_platform_windows_xp:
        assert lib_platform.system == 'windows'
        assert lib_platform.is_platform_windows
        assert not lib_platform.is_platform_windows_xp
        assert not lib_platform.is_platform_windows_wine
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_posix


def test_function_to_pickle():
    # type: () -> None
    if lib_platform.is_platform_windows:
        print('windows')
    if lib_platform.get_system() == 'windows':
        print('windows')


def test_if_pickable():
    # type: () -> None
    pickled_object = dill.dumps(test_function_to_pickle)
    unpickled_object = dill.loads(pickled_object)


def test_fake_xp_function():
    # type: () -> str
    return 'xp'


def test_fake_xp():
    # type: () -> None
    if lib_platform.is_platform_windows and not lib_platform.is_platform_windows_wine:
        save_platform_release_function = platform.release
        platform.release = test_fake_xp_function
        assert lib_platform.get_is_platform_windows_xp() is True
        assert lib_platform.get_system() == 'windows_xp'
        assert lib_platform.is_platform_windows
        assert not lib_platform.is_platform_windows_wine
        assert not lib_platform.is_platform_linux
        assert not lib_platform.is_platform_darwin
        assert not lib_platform.is_platform_posix
        platform.release = save_platform_release_function
