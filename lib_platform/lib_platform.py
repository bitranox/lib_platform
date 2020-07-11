# STDLIB
import ctypes
import getpass
import os
import platform
import socket
import subprocess


# OWN
import lib_registry


def get_hostname() -> str:
    """
    Returns fqdn hostname lowercase, also for WINE

    >>> result = get_hostname()
    >>> assert len(result) > 1

    """

    if get_is_platform_windows_wine():  # for wine get hostname not via IP Adress - would give name of the host
        # noinspection PyBroadException
        try:
            result_wine_reg = lib_registry.Registry().get_value(key=r'HKLM\System\CurrentControlSet\Control\ComputerName', value_name='ComputerName')
            assert isinstance(result_wine_reg, str)
            _hostname = result_wine_reg
        except Exception:
            result_wine_env = os.getenv('COMPUTERNAME')  # max 15 Zeichen
            if result_wine_env is None:
                raise RuntimeError('can not determine Username on Wine')
            else:
                _hostname = result_wine_env

    elif get_is_platform_windows():
        _hostname = socket.getfqdn()
    else:
        # this one failed on the first call sometimes - use now getfqdn() supports both IPv4 and IPv6. - and sometimes give WRONG HOSTNAME
        # _hostname = socket.gethostbyaddr(socket.gethostname())[0]

        # sometimes gives WRONG HOSTNAME on a bridge after reboot - WEIRD !
        # _hostname = socket.getfqdn()

        # this always works
        _hostname = subprocess.getoutput('uname -n')

    _hostname = str(_hostname.lower())
    return str(_hostname)


def get_hostname_short() -> str:
    """
    Returns hostname lowercase without domain part

    >>> result = get_hostname_short()
    >>> assert len(result) > 1

    """

    _hostname = get_hostname()
    _hostname_short = _hostname.split('.', 1)[0]
    return _hostname_short


def get_system() -> str:
    """
    gets system - but more detailed
    >>> result = get_system()
    >>> possible_results = ['darwin', 'linux', 'windows', 'windows_xp', 'windows_wine', 'windows_wine_xp']
    >>> assert result in possible_results
    """
    if get_is_platform_windows():
        s_system = _get_system_windows()
    else:
        s_system = platform.system().lower()
    return s_system


def _get_system_windows() -> str:
    _is_platform_windows_wine = get_is_platform_windows_wine()
    if _is_platform_windows_wine:
        s_system = _get_system_windows_wine()
    else:
        s_system = _get_system_windows_not_wine()
    return s_system


def _get_system_windows_wine() -> str:
    _is_platform_windows_xp = get_is_platform_windows_xp()
    if _is_platform_windows_xp:
        s_system = 'windows_wine_xp'
    else:
        s_system = 'windows_wine'
    return s_system


def _get_system_windows_not_wine() -> str:
    _is_platform_windows_xp = get_is_platform_windows_xp()
    if _is_platform_windows_xp:
        s_system = 'windows_xp'
    else:
        s_system = 'windows'
    return s_system


def get_username() -> str:
    """
    Returns username lowercase

    >>> username = get_username()
    >>> assert len(username) > 1

    """
    _username = getpass.getuser().lower()
    return _username


def get_is_platform_windows() -> bool:
    """
    >>> result = get_is_platform_windows()
    """
    is_platform_windows = platform.system().lower() == 'windows'
    return is_platform_windows


def get_is_platform_windows_xp() -> bool:
    """
    >>> result = get_is_platform_windows_xp()
    """

    if get_is_platform_windows() and platform.release().lower() == 'xp':
        return True
    else:
        return False


def get_is_platform_windows_wine() -> bool:
    """
    >>> result = get_is_platform_windows_wine()

    """

    if get_is_platform_windows():
        _is_platform_windows_wine = lib_registry.Registry().key_exist(r'HKEY_LOCAL_MACHINE\Software\Wine')
    else:
        _is_platform_windows_wine = False
    return bool(_is_platform_windows_wine)


def get_path_userhome() -> str:
    """
    >>> result = get_path_userhome()
    >>> assert len(result) > 1

    """

    s_userhome = os.path.realpath(os.path.expanduser("~"))
    return s_userhome


def get_is_user_admin() -> bool:

    """Return True if user has admin privileges.

    Raises:  AdminStateUnknownError under Windows if user privileges cannot be determined.


    >>> result = get_is_user_admin()
    >>> assert type(result) == bool

    """

    if get_is_platform_windows():
        # type ignore is needed here, because does not exist on linux
        _is_user_admin = ctypes.windll.shell32.IsUserAnAdmin() == 1   # type: ignore
    else:
        # type ignore is needed here, because os.getuid does not exist on windows
        _is_user_admin = os.getuid() == 0                             # type: ignore

    return bool(_is_user_admin)


def dummy_function() -> int:
    # to suppress 'unused type ignore' messages on strict mypy checking under linux
    return 42


is_platform_windows = get_is_platform_windows()
is_platform_linux = platform.system().lower() == 'linux'
is_platform_darwin = platform.system().lower() == 'darwin'
is_platform_posix = not get_is_platform_windows()
is_platform_windows_xp = get_is_platform_windows_xp()
is_platform_windows_wine = get_is_platform_windows_wine()
is_platform_windows_wine_xp = is_platform_windows_xp and is_platform_windows_wine
is_user_admin = get_is_user_admin()
# 'darwin', 'linux', 'windows', 'windows_xp', 'windows_wine', 'windows_wine_xp'
system = get_system()
username = get_username()
hostname = get_hostname()
hostname_short = get_hostname_short()
path_userhome = get_path_userhome()
