lib_platform
============

|travis_build| |license| |jupyter| |pypi|

|codecov| |better_code| |cc_maintain| |cc_issues| |cc_coverage| |snyk|


.. |travis_build| image:: https://img.shields.io/travis/bitranox/lib_platform/master.svg
   :target: https://travis-ci.org/bitranox/lib_platform

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/bitranox/lib_platform/master?filepath=lib_platform.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-platform?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_platform

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_platform
   :target: https://codecov.io/gh/bitranox/lib_platform

.. |better_code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_platform?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_platform

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_platform?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_platform/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_platform?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_platform/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_platform?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_platform/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/lib_platform
   :target: https://snyk.io/test/github/bitranox/lib_platform

some platform related functions, which also work correctly on wine

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3

`100% code coverage <https://codecov.io/gh/bitranox/lib_platform>`_, codestyle checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/lib_platform>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Installation and Upgrade`_
- `Usage`_
- `Usage from Commandline`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_platform/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_platform/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_platform/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=lib_platform.ipynb>`_

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools
    python -m pip --upgrade wheel

- to install the latest release from PyPi via pip (recommended):

.. code-block:: bash

    # install latest release from PyPi
    python -m pip install --upgrade lib_platform

    # test latest release from PyPi without installing (can be skipped)
    python -m pip install lib_platform --install-option test

- to install the latest development version from github via pip:


.. code-block:: bash

    # normal install
    python -m pip install --upgrade git+https://github.com/bitranox/lib_platform.git

    # to test without installing (can be skipped)
    python -m pip install git+https://github.com/bitranox/lib_platform.git --install-option test

    # to install and upgrade all dependencies regardless of version number
    python -m pip install --upgrade git+https://github.com/bitranox/lib_platform.git --upgrade-strategy eager


- include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_platform

    # for the latest development version :
    lib_platform @ git+https://github.com/bitranox/lib_platform.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt



- to install the latest development version from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_platform.git
    $ cd lib_platform

    # to test without installing (can be skipped)
    python setup.py test

    # normal install
    python setup.py install

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_platform.git
    $ cd lib_platform

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Usage
-----------

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

Usage from Commandline
------------------------

.. code-block:: bash

   Usage: lib_platform [OPTIONS] COMMAND [ARGS]...

     some platform related functions, which also work correctly on wine

   Options:
     --version   Show the version and exit.
     -h, --help  Show this message and exit.

   Commands:
     info  get program informations

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    lib_registry @ git+https://github.com/bitranox/lib_registry.git

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_platform/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

0.2.1
-----
2020-07-14 : patch release
    - make it compatible with latest lib_winreg


0.2.0
-----
2020-07-07 : service release
    - new click cli
    - use PizzaCutter Template
    - added jupyter notebook
    - dropped python2.7 - python3.5 support

1.0.3
-----
2019-06-14: add is_user_admin (check for administration rights)

1.0.2
-----
2019-04-28: Documentation Update, minor Fixes in setup.py

1.0.0
-----
2019-03-28: Initial public release, PyPi Release

