lib_platform
============

|Build Status| |jupyter| |Codecov Status| |Better Code| |snyk security|

some convenience functions used in many scripts

supports python 2.7 - python 3.7 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_platform>`_, tested under `Linux, OsX and Windows <https://travis-ci.org/bitranox/lib_platform>`_

-----


`Report Issues <https://github.com/bitranox/lib_platform/blob/master/ISSUE_TEMPLATE.md>`_

`Contribute <https://github.com/bitranox/lib_platform/blob/master/CONTRIBUTING.md>`_

`Pull Request <https://github.com/bitranox/lib_platform/blob/master/PULL_REQUEST_TEMPLATE.md>`_

`Code of Conduct <https://github.com/bitranox/lib_platform/blob/master/CODE_OF_CONDUCT.md>`_


-----

Try it in Jupyter Notebook
--------------------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/bitranox/lib_platform/master?filepath=jupyter_test_lib_platform.ipynb>`_


Installation and Upgrade
------------------------

From source code:

::

    python setup.py install
    python setup.py test

via pip (preferred):

::

    pip install --upgrade https://github.com/bitranox/lib_platform/archive/master.zip

via requirements.txt:

::

    Insert following line in Your requirements.txt:
    https://github.com/bitranox/lib_platform/archive/master.zip

    to install and upgrade all modules mentioned in requirements.txt:
    pip install --upgrade -r /<path>/requirements.txt

via python:

::

    python -m pip install --upgrade https://github.com/bitranox/lib_platform/archive/master.zip


Basic Usage
-----------

::

    >>> from lib_platform import *

    >>> # possible values : lowercase, returns:  'darwin', 'linux', 'windows', 'windows_xp', 'windows_wine'
    >>> system
    'linux'

    >>> is_platform_linux
    True

    >>> is_platform_darwin
    False

    >>> is_platform_posix       # either darwin or linux
    True

    >>> is_platform_windows     # also True for windows_xp or windows_wine
    False

    >>> is_platform_windows_xp
    False

    >>> is_platform_windows_wine
    False

    >>> username
    'root'

    >>> hostname
    'test.host.com'

    >>> hostname_short
    'test'

    >>> is_python2
    False

    >>> is_python3
    True

    >>> path_userhome
    '/home/user'

Requirements
------------

lib_registry, see: https://github.com/bitranox/lib_registry

pytest, see : https://github.com/pytest-dev/pytest

typing, see : https://pypi.org/project/typing/

Acknowledgement
---------------

special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
Please contribute.

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

See `License file <https://github.com/bitranox/lib_platform/blob/master/LICENSE.txt>`_

.. |Build Status| image:: https://travis-ci.org/bitranox/lib_platform.svg?branch=master
   :target: https://travis-ci.org/bitranox/lib_platform
.. |Codecov Status| image:: https://codecov.io/gh/bitranox/lib_platform/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_platform
.. |Better Code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_platform?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_platform
.. |snyk security| image:: https://snyk.io/test/github/bitranox/lib_platform/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_platform
.. |jupyter| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/bitranox/wrapt_timeout_decorator/master?filepath=jupyter_test_wrapt_timeout_decorator.ipynb
