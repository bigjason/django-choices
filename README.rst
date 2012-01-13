============================
Django-Choices
============================
Order and sanity for django model choices.
------------------------------------------------------
*Documentation is a work in progress.*

Django choices provides a declarative way of using the choices_ option on django_
fields.  More information on its development can be found at its `Home Page`_.

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
    class Person(models.Model):
    	# Choices
        class PersonType(DjangoChoices):
            Customer = ChoiceItem("C")
            Employee = ChoiceItem("E")
            Groundhog = ChoiceItem("G")
        # Fields
        name = models.CharField(max_length=32)
        type = models.CharField(max_length=1, choices=PersonType.choices)

You can use this elsewhere like this::

    # Other code
    Person.create(name="Phil", type=Person.PersonType.Groundhog)

The `DjangoChoices` classes can be located anywhere you want.  If I have a lot of
declarations I will sometimes place them in a `const.py` or `choices.py`.

-------
License
-------
Licensed under the `MIT License`_.

----------
Souce Code
----------
The source code can be found on github_.

.. _choices: http://docs.djangoproject.com/en/1.2/ref/models/fields/#choices
.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
.. _django: http://www.djangoproject.com/
.. _github: https://github.com/bigjason/django-choices
.. _PyPi: http://pypi.python.org/pypi/django-choices/
.. _Home Page: http://www.bigjason.com/projects/django-choices/