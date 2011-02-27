============================
Django-Choices
============================
Order and sanity for django model choices.
------------------------------------------------------
*Documentation is a work in progress.*

Django choices provides a declarative way of using the choices_ option on django_
fields.

-----------
Basic Usage
-----------
To start you create a choices class in choices.py or const.py (I prefer const.py).
Then you point the choices property to the ``choices`` attribute of the new class.
Django will be able to use the choices and you will be able to access the values
by name.  For example::

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