# STDLIB
import ctypes
import getpass
import os
import platform
import socket
import subprocess
import sys


is_platform_windows = platform.system().lower() == 'windows'

if is_platform_windows:
    import lib_registry


def get_hostname():
    # type: () -> str
    """
    :returns: fqdn hostname lowercase

    >>> result = get_hostname()
    >>> assert len(result) > 1

    """

    if get_is_platform_windows_wine():  # for wine get hostname not via IP Adress - would give name of the host
        # noinspection PyBroadException
        try:
            _hostname = lib_registry.get_value(key_name=r'HKLM\System\CurrentControlSet\Control\ComputerName',
                                               value_name='ComputerName')
        except Exception:
            _hostname = os.getenv('COMPUTERNAME')  # max 15 Zeichen
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


def get_hostname_short():
    # type: () -> str
    """
    :returns: hostname lowercase

    >>> result = get_hostname_short()
    >>> assert len(result) > 1

    """

    _hostname = get_hostname()
    _hostname_short = _hostname.split('.', 1)[0]
    return _hostname_short


def get_system():
    # type: () -> str
    """
    >>> result = get_system()
    >>> possible_results = ['darwin', 'linux', 'windows', 'windows_xp', 'windows_wine', 'windows_wine_xp']
    >>> assert result in possible_results
    """
    if is_platform_windows:
        s_system = _get_system_windows()
    else:
        s_system = platform.system().lower()
    return s_system


def _get_system_windows():
    # type: () -> str
    _is_platform_windows_wine = get_is_platform_windows_wine()
    if _is_platform_windows_wine:
        s_system = _get_system_windows_wine()
    else:
        s_system = _get_system_windows_not_wine()
    return s_system


def _get_system_windows_wine():
    # type: () -> str
    _is_platform_windows_xp = get_is_platform_windows_xp()
    if _is_platform_windows_xp:
        s_system = 'windows_wine_xp'
    else:
        s_system = 'windows_wine'
    return s_system


def _get_system_windows_not_wine():
    # type: () -> str
    _is_platform_windows_xp = get_is_platform_windows_xp()
    if _is_platform_windows_xp:
        s_system = 'windows_xp'
    else:
        s_system = 'windows'
    return s_system


def get_username():
    # type: () -> str
    """
    :returns: username lowercase

    >>> username = get_username()
    >>> assert len(username) > 1

    """
    _username = getpass.getuser().lower()
    return _username


def get_is_platform_windows():
    # type: () -> bool
    """
    >>> result = get_is_platform_windows()
    """

    if platform.system().lower() == 'windows':
        return True
    else:
        return False


def get_is_platform_windows_xp():
    # type: () -> bool

    if is_platform_windows and platform.release().lower() == 'xp':
        return True
    else:
        return False


def get_is_platform_windows_wine():
    # type: () -> bool
    """
    >>> result = get_is_platform_windows_wine()

    """

    if is_platform_windows:
        _is_platform_windows_wine = lib_registry.key_exist(r'HKEY_LOCAL_MACHINE\Software\Wine')
    else:
        _is_platform_windows_wine = False
    return bool(_is_platform_windows_wine)


def get_is_python_2():
    # type: () -> bool
    """
    >>> result = get_is_python_2()

    """

    if sys.version_info < (3, 0):
        return True
    else:
        return False


def get_path_userhome():
    # type: () -> str
    """
    >>> result = get_path_userhome()
    >>> assert len(result) > 1

    """

    s_userhome = os.path.realpath(os.path.expanduser("~"))
    return s_userhome


def get_is_user_admin():
    # type: () -> bool
    """Return True if user has admin privileges.

    Raises:
        AdminStateUnknownError if user privileges cannot be determined.

    >>> result = get_is_user_admin()
    >>> assert type(result) == bool

    """

    if get_is_platform_windows():
        _is_user_admin = ctypes.windll.shell32.IsUserAnAdmin() == 1   # type: ignore
    else:
        _is_user_admin = os.getuid() == 0                             # type: ignore
    return bool(_is_user_admin)


is_platform_windows = get_is_platform_windows()
is_platform_linux = platform.system().lower() == 'linux'              # type: bool
is_platform_darwin = platform.system().lower() == 'darwin'            # type: bool
is_platform_posix = not is_platform_windows                           # type: bool
is_platform_windows_xp = get_is_platform_windows_xp()                 # type: bool
is_platform_windows_wine = get_is_platform_windows_wine()             # type: bool
is_platform_windows_wine_xp = is_platform_windows_xp and is_platform_windows_wine       # type: bool
is_user_admin = get_is_user_admin()                                                     # type: bool
# 'darwin', 'linux', 'windows', 'windows_xp', 'windows_wine', 'windows_wine_xp'
system = get_system()                                                 # type: str
username = get_username()                                             # type: str
hostname = get_hostname()                                             # type: str
hostname_short = get_hostname_short()                                 # type: str
is_python2 = get_is_python_2()                                        # type: bool
is_python3 = not is_python2                                           # type: bool
path_userhome = get_path_userhome()                                   # type: str
