.. Django-Choices documentation master file, created by
   sphinx-quickstart on Thu Sep 10 22:03:38 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Django-Choices
==============

.. rubric:: Order and sanity for django model choices.

|build-status| |code-quality| |coverage| |docs| |black| |pypi| |python-versions| |django-versions|

Contents:

.. toctree::
   :maxdepth: 2

   migrating
   choices
   contributing

Overview
--------

.. warning::

    We **strongly** recommend migrating to the native functionality and not use
    django-choices for new projects. See the :ref:`migration`. This library will not be
    actively developed any longer.

Django choices provides a declarative way of using the choices_ option on django_ fields.

**Note:** Django 3.0 added `enumeration types <https://docs.djangoproject.com/en/3.0/releases/3.0/#enumerations-for-model-field-choices>`__.
This feature mostly replaces the need for Django-Choices.
See also `Adam Johnson's post on using them <https://adamj.eu/tech/2020/01/27/moving-to-django-3-field-choices-enumeration-types/>`__.


Requirements
------------

Django choices is fairly simple, so most Python and Django
versions should work. It is tested against Python 3.8+ and Django 3.2+.


Quick-start
-----------

Install like any other library:

.. code-block:: sh

   pip install django-choices

There is no need to add it in your installed apps.

To use it, you write a choices class, and use it in your model fields:


.. code-block:: python

    from djchoices import ChoiceItem, DjangoChoices


    class Book(models.Model):

        class BookType(DjangoChoices):
            short_story = ChoiceItem('short', 'Short story')
            novel = ChoiceItem('novel', 'Novel')
            non_fiction = ChoiceItem('non_fiction', 'Non fiction')


        author = models.ForeignKey('Author')
        book_type = models.CharField(
            max_length=20, choices=BookType.choices,
            default=BookType.novel
        )


You can then use the available choices in other modules, e.g.:


.. code-block:: python

    from .models import Book

    Person.objects.create(author=my_author, type=Book.BookTypes.short_story)


The ``DjangoChoices`` classes can be located anywhere you want,
for example you can put them outside of the model declaration if you have a
'common' set of choices for different models. Any place is valid though,
you can group them all together in ``choices.py`` if you want.


License
-------
Licensed under the `MIT License`_.

Source Code and contributing
----------------------------
The source code can be found on github_.

Bugs can also be reported on the github_ repository, and pull requests
are welcome. See :ref:`contributing` for more details.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

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

.. _django: http://www.djangoproject.com/
.. _choices: https://docs.djangoproject.com/en/dev/ref/models/fields/#choices
.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
.. _github: https://github.com/bigjason/django-choices
