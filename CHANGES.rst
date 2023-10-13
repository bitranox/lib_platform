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
