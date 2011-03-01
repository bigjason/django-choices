============================
Django-Choices
============================
Order and sanity for django model choices.
------------------------------------------------------
*Documentation is a work in progress.*

Django choices provides a declarative way of using the choices_ option on django_
fields.

-----------
Installation
-----------
You can install via PyPi_ or direct from the github_ repo.

To install with pip::

    $ pip install django-choices

To install with easy_install::

    $ easy_install django-choices

-----------
Basic Usage
-----------
To start you create a choices class somewhere.  I use const.py but you can just do 
it right on the model if you prefer. Then you point the choices property to the 
``choices`` attribute of the new class. Django will be able to use the choices and 
you will be able to access the values by name.  For example::

    # In choices.py 
    from djchoices import DjangoChoices, ChoiceItem
     
    class PersonType(DjangoChoices):
        Customer = ChoiceItem("C")
        Employee = ChoiceItem("E")
        Groundhog = ChoiceItem("G")

    # In models.py
    class Person(models.Model):
        name = models.CharField(max_length=32)
        type = models.CharField(max_length=1, choices=choices.PersonType.choices)
        
    # In other code
    Person.create(name="Phil", type=PersonType.Groundhog) 
       
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
