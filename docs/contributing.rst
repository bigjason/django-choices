.. _contributing:

Contributing
============

To get up and running quickly, fork the github repository and make all
your changes in your local clone.

Git-flow is prefered as git workflow, but as long as you make pull requests
against the `develop` branch, all should be well. Pull requests should
always have tests, and if relevant, documentation updates.

Feel free to create unfinished pull-requests to get the tests to build
and get work going, someone else might always want to pick up the tests
and/or documentation.


Testing
-------
For testing the standard unittest2 library is used, contrary to Django's
test framework. The reason is simple: speed. Django choices doesn't touch
the database in any way, so the standard library unit tests are fine.

To run the tests in your (virtual) environment, simple execute

.. code-block:: sh

    python runtests.py

This will run the tests with the current python version and Django version.

To run the tests on all supported python/Django versions, use tox_.

.. code-block:: sh

    pip install tox
    tox

If you want to speed this up, you can also use detox_. This library will
run as much in parallel as possible.


Documentation
-------------

The documentation is built with Sphinx. Run `make` to build the documentation:

.. code-block: sh

    cd docs/
    make html

You can now open `_build/index.html`.


Coding style
------------
Please stick to PEP8, and use pylint or similar tools to check the code style.


.. _tox: https://testrun.org/tox/latest/
.. _detox: https://pypi.python.org/pypi/detox/
