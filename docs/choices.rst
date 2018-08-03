Choice items
============

The ``ChoiceItem`` class is what drives the choices. Each instance
corresponds to a possible choice for your field.


Basic usage
-----------

.. code-block:: python

    class MyChoices(DjangoChoices):
        my_choice = ChoiceItem(1, 'label 1')


The first argument for ``ChoiceItem`` is the value, as it will be stored
in the database. ``ChoiceItem`` values can be any type, as long as it matches
the field where the choices are defined, e.g.:

String type:

.. code-block:: python

    class Strings(DjangoChoices):
        one = ChoiceItem('one', 'one')


    class Model1(models.Model):
        field = models.CharField(max_length=10, choices=Strings.choices)


or integer:

.. code-block:: python

    class Ints(DjangoChoices):
        one = ChoiceItem(1, 'one')


    class Model2(models.Model):
        field = models.IntegerField(choices=Ints.choices)


There is also a 'short name'. You can import ``C`` instead of `ChoiceItem`, if
you're into that.

Custom attributes
+++++++++++++++++

Any additional (custom) keyword arguments passed to the constructor, are made
available as custom attributes:

.. code-block:: python

    >>> choice = ChoiceItem('excellent', limit_to=['US', 'CA', 'CN'])
    >>> choice.limit_to
    ['US', 'CA', "CN"]

To obtain the ``ChoiceItem`` instance, see :ref:`djangochoices.get_choice`


Labels
------
The second argument to the `ChoiceItem` class is the label.
It's recommended to specify this explicitly if you use
internationalization, e.g.:


.. code-block:: python

    from django.utils.translation import ugettext_lazy as _


    class MyChoices(DjangoChoices):
        one = ChoiceItem(1, _('one'))


If the label is not provided, it will be automatically determined from
the class property, and underscores are translated to spaces. So, the
following example yields:

.. code-block:: python

    >>> class MyChoices(DjangoChoices):
    ...     first_choice = ChoiceItem(1)

    >>> MyChoices.choices
    ((1, 'first choice'),)


Ordering
--------

`ChoiceItem` objects also support ordering. If not provided, the choices are
returned in order of declaration.


.. code-block:: python

    >>> class MyChoices(DjangoChoices):
    ...     first = ChoiceItem(1, order=20)
    ...     second = ChoiceItem(2, order=10)

    >>> MyChoices.choices
    (
        (2, 'second'),
        (1, 'first'),
    )


Values
------
If you really want to use the minimal amount of code, you can leave off the
value as well, and it will be determined from the label.

.. code-block:: python

    >>> class Sample(DjangoChoices):
    ...     OptionA = ChoiceItem()
    ...     OptionB = ChoiceItem()

    >>> Sample.choices
    (
        ('OptionA', 'OptionA'),
        ('OptionB', 'OptionB'),
    )


``DjangoChoices`` class attributes
----------------------------------

The choices class itself has a few useful attributes. Most notably `choices`,
which returns the choices as a tuple.


choices
+++++++

.. code-block:: python

    >>> class Sample(DjangoChoices):
    ...     OptionA = ChoiceItem()
    ...     OptionB = ChoiceItem()

    >>> Sample.choices
    (
        ('OptionA', 'OptionA'),
        ('OptionB', 'OptionB'),
    )


labels
++++++

Returns a dictionary with a mapping from attribute to the human-readable
label:

.. code-block:: python

    >>> class MyChoices(DjangoChoices):
    ...     first_choice = ChoiceItem(1)
    ...     second_choice = ChoiceItem(2)

    >>> MyChoices.labels
    {'first_choice': 1, 'second_choice': 2}
    >>> MyChoices.labels.first_choice
    "first choice"


values
++++++

Returns a dictionary with a mapping from value to label:

.. code-block:: python

    >>> class MyChoices(DjangoChoices):
    ...     first_choice = ChoiceItem(1, 'label 1')
    ...     second_choice = ChoiceItem(2, 'label 2')

    >>> MyChoices.values
    {1: 'label 1', '2': 'label 2'}


validator
+++++++++

.. note::

    At least since Django 1.3, there is model and form-level validation of the
    choices. Unless you have a reason to explicitly specify/override the validator,
    you can skip specifying this validator.


Returns a validator that can be used in your model field. This validator checks
that the value passed to the field is indeed a value specified in your choices
class.

attributes
++++++++++

Returns an ``OrderedDict`` with the mapping from choice value -> attribute
on the choices class.

.. code-block:: python

    >>> class MyChoices(DjangoChoices):
    ...     first_choice = ChoiceItem(1, 'label 1')
    ...     second_choice = ChoiceItem(2, 'label 2')

    >>> MyChoices.attributes
    OrderedDict([(1, 'first_choice'), (2, 'second_choice')])


.. _djangochoices.get_choice:

get_choice
++++++++++

Returns the actual ``ChoiceItem`` instance for a given value:

.. code-block:: python

    >>> class MyChoices(DjangoChoices):
    ...     first_choice = ChoiceItem(1, 'label 1')
    ...     second_choice = ChoiceItem(2, 'label 2')

    >>> MyChoices.get_choice(MyChoices.second_choice)
    <ChoiceItem value=2 label='label 2' order=1>

This allows you to inspect any ``ChoiceItem`` attributes.
