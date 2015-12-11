.. Django-Choices documentation master file, created by
   sphinx-quickstart on Thu Sep 10 22:03:38 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Django-Choices
==============

.. rubric:: Order and sanity for django model choices.

.. image:: https://travis-ci.org/bigjason/django-choices.png
    :target: http://travis-ci.org/bigjason/django-choices

.. image:: https://coveralls.io/repos/bigjason/django-choices/badge.svg
    :target: https://coveralls.io/github/bigjason/django-choices?branch=master

.. image:: https://img.shields.io/pypi/v/django-choices.svg
  :target: https://pypi.python.org/pypi/django-choices


Contents:

.. toctree::
   :maxdepth: 2

   choices
   contributing

Overview
--------

Django choices provides a declarative way of using the
choices_ option on django_ fields.


Requirements
------------

Django choices is fairly simple, so most Python and Django
versions should work. Django choices is tested against Python
2.6, 2.7, 3.3, 3.4 and PyPy. Django 1.3 until 1.8 (including)
are officially supported.


Quick-start
-----------

Install like any other library:

.. code-block:: sh

   pip install django-choices

There is no need to add it in your installed apps.

To use it, you write a choices class, and use it in your model fields:


.. code-block:: python

    from djchoices import DjangoChoices, ChoiceItem


    class Book(models.Model):

        class BookTypes(DjangoChoices):
            short_story = ChoiceItem('short', 'Short story')
            novel = ChoiceItem('novel', 'Novel')
            non_fiction = ChoiceItem('non_fiction', 'Non fiction')


        author = models.ForeignKey('Author')
        book_type = models.CharField(
            max_length=20, choices=BookTypes.choices,
            default=BookTypes.novel, validators=[BookTypes.validator]
        )


You can use this in other places like this:


.. code-block:: python

    from .models import Book


    Person.objects.create(author=my_author, type=Book.BookTypes.short_story)


The `DjangoChoices` classes can be located anywhere you want,
for example you can put them outside of the model declaration if you have a
'common' set of choices for different models. Any place is valid though,
you can group them all together in `choices.py` if you want.

License
-------
Licensed under the `MIT License`_.

Souce Code and contributing
---------------------------
The source code can be found on github_.

Bugs can also be reported on the github_ repository, and pull requests
are welcome. See :ref:`contributing` for more details.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _django: http://www.djangoproject.com/
.. _choices: https://docs.djangoproject.com/en/dev/ref/models/fields/#choices
.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
.. _github: https://github.com/bigjason/django-choices
