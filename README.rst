lib_platform
============


Version v1.2.10 as of 2023-10-13 see `Changelog`_

|build_badge| |codeql| |license| |jupyter| |pypi|
|pypi-downloads| |black| |codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/lib_platform/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/lib_platform/actions/workflows/python-package.yml


.. |codeql| image:: https://github.com/bitranox/lib_platform/actions/workflows/codeql-analysis.yml/badge.svg?event=push
   :target: https://github.com//bitranox/lib_platform/actions/workflows/codeql-analysis.yml

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_platform/master?filepath=lib_platform.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-platform?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_platform

.. badge until 2023-10-08:
.. https://img.shields.io/codecov/c/github/bitranox/lib_platform
.. badge from 2023-10-08:
.. |codecov| image:: https://codecov.io/gh/bitranox/lib_platform/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_platform

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_platform?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_platform/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_platform?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_platform/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_platform?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_platform/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/lib_platform/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_platform

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/lib-platform
   :target: https://pypi.org/project/lib-platform/
   :alt: PyPI - Downloads

some platform related functions, which also work correctly on wine

----

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.8, 3.9, 3.10, 3.11, 3.12-dev, pypy-3.9, pypy-3.10 - architectures: amd64

`100% code coverage <https://codeclimate.com/github/bitranox/lib_platform/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/lib_platform/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
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

.. code-block::

   Usage: lib_platform [OPTIONS] COMMAND [ARGS]...

     some platform related functions, which also work correctly on wine

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block::

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade lib_platform


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade lib_platform[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/lib_platform.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_platform

    # for the latest development version :
    lib_platform @ git+https://github.com/bitranox/lib_platform.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/lib_platform.git
    $ cd lib_platform
    python -m pip install -e .[test]

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

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools
    lib_registry

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

v1.2.10
--------
2023-10-13:
    - patch doctest for osx

v1.2.9
--------
2023-07-21:
    - require minimum python 3.8
    - remove python 3.7 tests
    - introduce PEP517 packaging standard
    - introduce pyproject.toml build-system
    - remove mypy.ini
    - remove pytest.ini
    - remove setup.cfg
    - remove setup.py
    - remove .bettercodehub.yml
    - remove .travis.yml
    - update black config
    - clean ./tests/test_cli.py
    - add codeql badge
    - move 3rd_party_stubs outside the src directory to ``./.3rd_party_stubs``
    - add pypy 3.10 tests
    - add python 3.12-dev tests

v1.2.8
--------
2022-11-09:
    - fix get hostname, if something is tinkering with the loopback interface on Windows - for instance 'Solid Works 3DExperience'

v1.2.7
--------
2020-10-09: service release
    - update travis build matrix for linux 3.9-dev
    - update travis build matrix (paths) for windows 3.9 / 3.10

v1.2.6
--------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v1.2.5
---------
2020-08-01: fix pypi deploy

v1.2.4
--------
2020-07-31: fix travis build

v1.2.3
--------
2020-07-29: feature release
    - use the new pizzacutter template
    - use cli_exit_tools

v1.2.2
--------
2020-07-16: feature release
    - fix cli test
    - enable traceback option on cli errors

v1.2.1
--------
2020-07-14 : patch release
    - make it compatible with latest lib_registry


v1.2.0
--------
2020-07-07 : service release
    - new click cli
    - use PizzaCutter Template
    - added jupyter notebook
    - dropped python2.7 - python3.5 support

v1.0.3
--------
2019-06-14: add is_user_admin (check for administration rights)

v1.0.2
--------
2019-04-28: Documentation Update, minor Fixes in setup.py

v1.0.0
--------
2019-03-28: Initial public release, PyPi Release

