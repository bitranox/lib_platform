.. code-block:: python

    >>> import lib_platform

    >>> # get system as string
    >>> system = lib_platform.system

    >>> # bool is_platform_linux
    >>> is_platform_linux = lib_platform.is_platform_linux

    >>> # bool is_platform_darwin
    >>> is_platform_darwin = lib_platform.is_platform_darwin

    >>> # bool is_platform_posix
    >>> # either darwin or linux
    >>> is_platform_posix = lib_platform.is_platform_posix

    >>> # bool is_platform_windows
    >>> # also True for windows_xp or windows_wine
    >>> is_platform_windows = lib_platform.is_platform_windows

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

    >>> # path to userhome
    >>> path_userhome = lib_platform.path_userhome

    >>> # is user administrator (has user admin rights)
    >>> is_user_admin = lib_platform.is_user_admin
