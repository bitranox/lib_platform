lib_platform
============

|Pypi Status| |license| |maintenance| |jupyter|

|Build Status| |Codecov Status| |Better Code| |code climate| |snyk security|

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License
.. |maintenance| image:: https://img.shields.io/maintenance/yes/2019.svg
.. |Build Status| image:: https://travis-ci.org/bitranox/lib_platform.svg?branch=master
   :target: https://travis-ci.org/bitranox/lib_platform
.. for the pypi status link note the dashes, not the underscore !
.. |Pypi Status| image:: https://badge.fury.io/py/lib-platform.svg
   :target: https://badge.fury.io/py/lib_platform
.. |Codecov Status| image:: https://codecov.io/gh/bitranox/lib_platform/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_platform
.. |Better Code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_platform?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_platform
.. |snyk security| image:: https://snyk.io/test/github/bitranox/lib_platform/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_platform
.. |jupyter| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_platform/master?filepath=jupyter_test_lib_platform.ipynb
.. |code climate| image:: https://api.codeclimate.com/v1/badges/15acaf0e7747a042c505/maintainability
   :target: https://codeclimate.com/github/bitranox/lib_platform/maintainability
   :alt: Maintainability

some convenience functions used in many scripts

supports python 2.7 - python 3.7, pypy and possibly other dialects.

this is also a working example for travis.yml for multi-platform testing :

- install WINE
- install python 2.7 on wine 32 Bit
- install python 2.7 on wine 64 Bit
- install python 3.7 on wine 32 Bit
- install python 3.7 on wine 64 Bit
- run pytest on wine (all Versions mentioned above)
- run code coverage on wine (all Versions mentioned above)
- osx Build for Python 2.7, Python 3.7
- pypy Build for Python 2.7, Python 3.7
- Windows Build Python 2.7
- Windows Build Python 3.7
- build rst documentation with rst_include for github and PyPi

`100% code coverage <https://codecov.io/gh/bitranox/lib_platform>`_, mypy static type checking, tested under `Linux, OsX, Windows and Wine <https://travis-ci.org/bitranox/lib_platform>`_, automatic daily builds  and monitoring

----

- `Try it Online`_
- `Installation and Upgrade`_
- `Basic Usage`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_platform/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_platform/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_platform/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/bitranox/lib_platform/master?filepath=jupyter_test_lib_platform.ipynb>`_

Installation and Upgrade
------------------------

From source code:

.. code-block:: bash

    # normal install
    python setup.py install
    # test without installing
    python setup.py test

via pip latest Release:

.. code-block:: bash

    # latest Release from pypi
    pip install lib_platform

    # test without installing
    pip install lib_platform --install-option test

via pip latest Development Version:

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    pip install --upgrade https://github.com/bitranox/lib_platform/archive/master.zip --upgrade-strategy eager
    # normal install
    pip install --upgrade https://github.com/bitranox/lib_platform/archive/master.zip
    # test without installing
    pip install https://github.com/bitranox/lib_platform/archive/master.zip --install-option test

via requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release:
    lib_platform
    # for the latest Development Version :
    https://github.com/bitranox/lib_platform/archive/master.zip

    # to install and upgrade all modules mentioned in requirements.txt:
    pip install --upgrade -r /<path>/requirements.txt

via python:

.. code-block:: python

    # for the latest Release
    python -m pip install upgrade lib_platform

    # for the latest Development Version
    python -m pip install upgrade https://github.com/bitranox/lib_platform/archive/master.zip

Basic Usage
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

Requirements
------------

following modules will be automatically installed :

.. code-block:: shell

    pytest          # see : https://github.com/pytest-dev/pytest
    typing          # see : https://pypi.org/project/typing/
    lib_registry    # see: https://pypi.org/project/lib-registry/

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

