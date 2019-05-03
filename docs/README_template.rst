lib_platform
============

.. include:: ./badges_with_jupyter.rst

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


.. include:: ./tested_under.rst

----

- `Try it Online`_
- `Installation and Upgrade`_
- `Basic Usage`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/{repository_slug}/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/{repository_slug}/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/{repository_slug}/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_

----

Try it Online
-------------

.. include:: ./try_in_jupyter.rst

Installation and Upgrade
------------------------

.. include:: ./installation.rst


Basic Usage
-----------

.. include:: ../lib_platform/tests/test_lib_platform.py
    :code: python
    :start-after: >>> ### do not remove this line - marker doc basic usage start
    :end-before: >>> ### do not remove this line - marker doc basic usage end

Requirements
------------

following modules will be automatically installed :

.. include:: ../requirements.txt
        :code: shell

Acknowledgements
----------------
.. include:: ./acknowledgment.rst

Contribute
----------
.. include:: ./contribute.rst

License
-------
.. include:: ./licence_mit.rst
