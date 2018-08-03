============================
Django-Choices
============================

|travis| |coverage| |docs| |pypi| |python-versions| |django-versions|

Order and sanity for django model choices.
------------------------------------------------------

Django choices provides a declarative way of using the choices_ option on django_
fields. Read the full `documentation`_ on ReadTheDocs.

------------
Installation
------------
You can install via PyPi_ or direct from the github_ repo.

To install with pip:

.. code-block:: bash

    $ pip install django-choices

To install with easy_install:

.. code-block:: bash

    $ easy_install django-choices

-----------
Basic Usage
-----------
To start you create a choices class. Then you point the choices property on your
fields to the ``choices`` attribute of the new class. Django will be able to use
the choices and you will be able to access the values by name.  For example you
can replace this:

.. code-block:: python

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

With this:

.. code-block:: python

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

You can use this elsewhere like this:

.. code-block:: python

    # Other code
    Person.create(name="Phil", type=Person.PersonType.groundhog)

You can use them without value, and the label will be used as value:

.. code-block:: python

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

.. |travis| image:: https://secure.travis-ci.org/bigjason/django-choices.svg?branch=master
    :target: http://travis-ci.org/bigjason/django-choices

.. |coverage| image:: https://coveralls.io/repos/bigjason/django-choices/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/bigjason/django-choices?branch=master

.. |docs| image:: https://readthedocs.org/projects/django-choices/badge/?version=latest
    :target: http://django-choices.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |pypi| image:: https://img.shields.io/pypi/v/django-choices.svg
    :target: https://pypi.python.org/pypi/django-choices

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/django-choices.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/django-choices.svg

.. _choices: http://docs.djangoproject.com/en/stable/ref/models/fields/#choices
.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
.. _django: http://www.djangoproject.com/
.. _github: https://github.com/bigjason/django-choices
.. _PyPi: http://pypi.python.org/pypi/django-choices/
.. _documentation: http://django-choices.readthedocs.io/en/latest/
