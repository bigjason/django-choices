==============
Django-Choices
==============

|build-status| |code-quality| |coverage| |docs| |black| |pypi| |python-versions| |django-versions|

Order and sanity for django model choices.
------------------------------------------

**DISCLAIMER**

New projects should not use this package. Existing users can follow the migration guide
in the `documentation`_.

**Note:** Django 3.0 added `enumeration types <https://docs.djangoproject.com/en/3.0/releases/3.0/#enumerations-for-model-field-choices>`__.
This feature mostly replaces the need for Django-Choices.
See also `Adam Johnson's post on using them <https://adamj.eu/tech/2020/01/27/moving-to-django-3-field-choices-enumeration-types/>`__.

**Introduction**

Django choices provides a declarative way of using the choices_ option on django_
fields.

See the `documentation`_ on ReadTheDocs on how to use this library.

-------
License
-------

Licensed under the `MIT License`_.

-----------
Source Code
-----------

The source code can be found on github_.

.. |build-status| image:: https://github.com/bigjason/django-choices/actions/workflows/ci.yml/badge.svg
    :alt: Build status
    :target: https://github.com/bigjason/django-choices/actions/workflows/ci.yml

.. |code-quality| image:: https://github.com/bigjason/django-choices/actions//workflows/code_quality.yml/badge.svg
    :alt: Code quality checks
    :target: https://github.com/bigjason/django-choices/actions//workflows/code_quality.yml

.. |coverage| image:: https://codecov.io/gh/bigjason/django-choices/branch/master/graph/badge.svg?token=pcbBUCju0B
    :alt: Code coverage
    :target: https://codecov.io/gh/bigjason/django-choices

.. |docs| image:: https://readthedocs.org/projects/django-choices/badge/?version=latest
    :target: http://django-choices.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |pypi| image:: https://img.shields.io/pypi/v/django-choices.svg
    :target: https://pypi.python.org/pypi/django-choices

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/django-choices.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/django-choices.svg

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. _choices: https://docs.djangoproject.com/en/stable/ref/models/fields/#choices
.. _MIT License: https://en.wikipedia.org/wiki/MIT_License
.. _django: https://www.djangoproject.com/
.. _github: https://github.com/bigjason/django-choices
.. _PyPi: https://pypi.org/project/django-choices/
.. _documentation: https://django-choices.readthedocs.io/en/latest/
