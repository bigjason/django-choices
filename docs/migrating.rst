.. _migration:

Migrating to native Django Choices
==================================

Since version 3.0, Django offers native choices enums (mostly equivalent) to the
functionality that this library offers. See the `django docs`_ for more details.

We provide some automated tooling to facilitate migrating and instructions for possible
hurdles.

Generating equivalent native code
---------------------------------

For trivial usage where you just define the choices as a constant, there is a management
command since version 2.0 to generate the equivalent code. It supports ``str`` and ``int``
for values types.

#. Ensure you have ``djchoices`` added to your ``INSTALLED_APPS`` setting.
#. Run the command ``python manage.py generate_native_django_choices``

The command essentially discovers all subclasses of ``DjangoChoices`` and introspects
them to generate the equivalent native choices code. This depends on the classes being
imported during Django's initialization phase. This should be the case for almost all
usages, as the choices need to be imported to be picked up by models.

Possible options for the command:

* ``--no-wrap-gettext``: do not wrap the choice labels in a function call to mark them
  translatable.

* ``--gettext-alias``: when wrapping the labels, you can specify the name of the
  function call/alias to wrap with, e.g. ``gettext_lazy``. It defaults to the common
  pattern of ``_``. You need to ensure the necessary imports are present in the module.

Public API
----------

* The ``choices`` class attribute behaves the same in native choices.

Migrating non-trivial usage
---------------------------

Django-choices offered some class attributes that need to be updated too when migrating
to native choices.


``DjangoChoices.labels``
^^^^^^^^^^^^^^^^^^^^^^^^

This is roughly equivalent to:

.. code-block:: python

    dict(zip(Native.names, Native.labels))

Notable differences:

* for a value like ``'option1'`` without explicit label, Django Choices produces
  ``'option1'`` as label, while Django produces ``'option 1'``. A value like
  ``'option_1'`` results in the same label.
* It may not play nice with the empty option in native choices.


``ChoiceItem.order``
^^^^^^^^^^^^^^^^^^^^

The management command emits the generated native choices in the configured order.

If you need access to the order, you can leverage ``enumerate(Native.values)`` to loop
over tuples of ``(order, value)``.

``DjangoChoices.values``
^^^^^^^^^^^^^^^^^^^^^^^^

This is equivalent to:

.. code-block:: python

    dict(zip(Native.values, Native.labels))


``DjangoChoices.validator``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django has been performing this out of the box on model fields since at least
Django 1.3 - you don't need it.

``DjangoChoices.attributes``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is roughly equivalent to:

.. code-block:: python

    native = dict(zip(Native.values, Native.names))

Remarks:

* It may not play nice with the empty option in native choices.

``DjangoChoices.get_choice``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no direct equivalent, however you can access the enum instance and look up
properties:

.. code-block:: python

    an_enum_value = Native[Native.some_value]
    print(an_enum_value.value)
    print(an_enum_value.label)

``DjangoChoices.get_order_expression``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no equivalent, but you should easily be able to add this as your own
class method/mixin:

.. code-block:: python

    from django.db.models import Case, IntegerField, Value, When

    @classmethod
    def get_order_expression(cls, field_name):
        whens = []
        for order, value in enumerate(cls.values()):
            whens.append(
                When(**{field_name: value, "then": Value(order)})
            )
        return Case(*whens, output_field=IntegerField())

Custom attributes
^^^^^^^^^^^^^^^^^

It's recommended to keep a separate dictionary with a mapping of choice values to the
additional attributes. You could consider dataclasses to model this too.


.. _django docs: https://docs.djangoproject.com/en/3.2/ref/models/fields/#enumeration-types
