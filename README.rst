============================
Django-Choices
============================

.. image:: https://secure.travis-ci.org/bigjason/django-choices.svg?branch=master
    :target: http://travis-ci.org/bigjason/django-choices

.. image:: https://coveralls.io/repos/bigjason/django-choices/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/bigjason/django-choices?branch=master

.. image:: https://readthedocs.org/projects/django-choices/badge/?version=latest
    :target: http://django-choices.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/django-choices.svg
  :target: https://pypi.python.org/pypi/django-choices

Order and sanity for django model choices.
------------------------------------------------------

Django choices provides a declarative way of using the choices_ option on django_
fields. Read the full `documentation`_ on ReadTheDocs.

------------
Installation
------------
You can install via PyPi_ or direct from the github_ repo.

To install with pip::

    $ pip install django-choices

To install with easy_install::

    $ easy_install django-choices

-----------
Basic Usage
-----------
To start you create a choices class. Then you point the choices property on your
fields to the ``choices`` attribute of the new class. Django will be able to use
the choices and you will be able to access the values by name.  For example you
can replace this::

    # In models.py
    class Person(models.Model):
    	# Choices
    	PERSON_TYPE = (
            ("C", "Customer"),
            ("E", "Employee"),
            ("G", "Groundhog"),
        )
        # Fields
        name = models.CharField(max_length=32)
        type = models.CharField(max_length=1, choices=PERSON_TYPE)

With this::

    # In models.py
    from djchoices import DjangoChoices, ChoiceItem

    class Person(models.Model):
    	# Choices
        class PersonType(DjangoChoices):
            customer = ChoiceItem("C")
            employee = ChoiceItem("E")
            groundhog = ChoiceItem("G")

        # Fields
        name = models.CharField(max_length=32)
        type = models.CharField(max_length=1, choices=PersonType.choices)

You can use this elsewhere like this::

    # Other code
    Person.create(name="Phil", type=Person.PersonType.groundhog)

You can use them without value, and the label will be used as value::

    class Sample(DjangoChoices):
        option_a = ChoiceItem()
        option_b = ChoiceItem()

    print(Sample.option_a)  # "option_a"

-------
License
-------
Licensed under the `MIT License`_.

----------
Souce Code
----------
The source code can be found on github_.

.. _choices: http://docs.djangoproject.com/en/1.8/ref/models/fields/#choices
.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
.. _django: http://www.djangoproject.com/
.. _github: https://github.com/bigjason/django-choices
.. _PyPi: http://pypi.python.org/pypi/django-choices/
.. _documentation: http://django-choices.readthedocs.io/en/latest/
