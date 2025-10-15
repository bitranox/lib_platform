# STDLIB
import ctypes
import getpass
from functools import lru_cache
import os
import platform
import socket
import subprocess


# OWN
# import lib_registry  --> lazy loading by intent


@lru_cache(maxsize=None)
def get_hostname() -> str:
    """
    Returns fqdn hostname lowercase, also for WINE

    >>> result = get_hostname()
    >>> assert len(result) > 1
    """

    if get_is_platform_windows_wine():  # for wine get hostname not via IP Adress - that would give name of the linux host
        # noinspection PyBroadException
        try:
            import lib_registry     # lazy loading by intent
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
        _hostname = _get_fqdn_by_hostname()
    else:
        # this one failed on the first call sometimes - use now getfqdn() supports both IPv4 and IPv6. - and sometimes give WRONG HOSTNAME
        # _hostname = socket.gethostbyaddr(socket.gethostname())[0]

        # sometimes gives WRONG HOSTNAME on a bridge after reboot - WEIRD !
        # _hostname = socket.getfqdn()

        # this always works
        _hostname = subprocess.getoutput('uname -n')

    return str(_hostname.lower())


@lru_cache(maxsize=None)
def _get_fqdn_by_hostname() -> str:
    """
    Returns fqdn by hostname - will be only used on windows
    if You use just socket.getfqdn(), it will return 'dslauncher.3ds.com' if Solid Works 3DExperience is installed.
    this is because they tinker with the loopback address
    therefore we get hostname --> ip adress --> fqdn

    >>> if get_is_platform_windows(): \
            assert _get_fqdn_by_hostname() is not None

    """
    _hostname_short = socket.gethostname()
    _ip_address = socket.gethostbyname(_hostname_short)
    _fqdn = socket.getfqdn(name=_ip_address)
    return _fqdn


@lru_cache(maxsize=None)
def get_hostname_short() -> str:
    """
    Returns hostname lowercase without domain part

    >>> result = get_hostname_short()
    >>> assert len(result) > 1

    """

    _hostname = get_hostname()
    _hostname_short = _hostname.split('.', 1)[0]
    return _hostname_short


@lru_cache(maxsize=None)
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


@lru_cache(maxsize=None)
def _get_system_windows() -> str:
    _is_platform_windows_wine = get_is_platform_windows_wine()
    if _is_platform_windows_wine:
        s_system = _get_system_windows_wine()
    else:
        s_system = _get_system_windows_not_wine()
    return s_system


@lru_cache(maxsize=None)
def _get_system_windows_wine() -> str:
    _is_platform_windows_xp = get_is_platform_windows_xp()
    if _is_platform_windows_xp:
        s_system = 'windows_wine_xp'
    else:
        s_system = 'windows_wine'
    return s_system


@lru_cache(maxsize=None)
def _get_system_windows_not_wine() -> str:
    _is_platform_windows_xp = get_is_platform_windows_xp()
    if _is_platform_windows_xp:
        s_system = 'windows_xp'
    else:
        s_system = 'windows'
    return s_system


@lru_cache(maxsize=None)
def get_username() -> str:
    """
    Returns username lowercase

    >>> username = get_username()
    >>> assert len(username) > 1

    """
    _username = getpass.getuser().lower()
    return _username


@lru_cache(maxsize=None)
def get_is_platform_windows() -> bool:
    """
    >>> result = get_is_platform_windows()
    """
    is_platform_windows = platform.system().lower() == 'windows'
    return is_platform_windows


@lru_cache(maxsize=None)
def get_is_platform_windows_xp() -> bool:
    """
    >>> result = get_is_platform_windows_xp()
    """

    if get_is_platform_windows():
        if platform.release().lower() == 'xp':
            return True
        system_lower = platform.system().lower()
        if "_xp" in system_lower:
            return True
    return False


@lru_cache(maxsize=None)
def get_is_platform_windows_wine() -> bool:
    """
    >>> result = get_is_platform_windows_wine()

    """

    if get_is_platform_windows():
        import lib_registry  # lazy loading by intent
        _is_platform_windows_wine = lib_registry.Registry().key_exist(r'HKEY_LOCAL_MACHINE\Software\Wine')
    else:
        _is_platform_windows_wine = False
    return bool(_is_platform_windows_wine)


@lru_cache(maxsize=None)
def get_path_userhome() -> str:
    """
    >>> result = get_path_userhome()
    >>> assert len(result) > 1

    """

    s_userhome = os.path.realpath(os.path.expanduser("~"))
    return s_userhome


@lru_cache(maxsize=None)
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
        # type ignore is needed here, because does not exist on windows
        _is_user_admin = os.getuid() == 0                             # type: ignore

    return bool(_is_user_admin)


@lru_cache(maxsize=None)
def get_is_platform_windows_wine_xp() -> bool:
    return get_is_platform_windows_xp() and get_is_platform_windows_wine()


@lru_cache(maxsize=None)
def get_is_platform_linux() -> bool:
    return get_system().lower() == 'linux'


@lru_cache(maxsize=None)
def get_is_platform_darwin() -> bool:
    return get_system().lower() == 'darwin'


@lru_cache(maxsize=None)
def get_is_platform_posix() -> bool:
    return not get_is_platform_windows()
