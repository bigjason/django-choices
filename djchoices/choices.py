from __future__ import absolute_import, unicode_literals

import re
from collections import OrderedDict

from django.core.exceptions import ValidationError
from django.db.models import Case, IntegerField, Value, When
from django.utils.deconstruct import deconstructible

import six

__all__ = ["ChoiceItem", "DjangoChoices", "C"]


# Support Functionality (Not part of public API)


class Labels(dict):
    def __getattr__(self, name):
        result = dict.get(self, name, None)
        if result is not None:
            return result
        else:
            raise AttributeError("Label for field %s was not found." % name)

    def __setattr__(self, name, value):
        self[name] = value


class StaticProp(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, objtype):
        return self.value


class Attributes(object):
    def __init__(self, attrs, fields):
        self.attrs = attrs
        self.fields = fields

    def __get__(self, obj, objtype):
        if len(self.attrs) != len(self.fields):
            raise ValueError(
                "Not all values are unique, it's not possible to map all "
                "values to the right attribute"
            )
        return self.attrs


# End Support Functionality


sentinel = object()


class ChoiceItem(object):
    """
    Describes a choice item.

    The label is usually the field name so label can normally be left blank.
    Set a label if you need characters that are illegal in a python identifier
    name (ie: "DVD/Movie").
    """

    order = 0

    def __init__(self, value=sentinel, label=None, order=None, **extra):
        self.value = value
        self.label = label
        self._extra = extra

        if order is not None:
            self.order = order
        else:
            ChoiceItem.order += 1
            self.order = ChoiceItem.order

    def __repr__(self):
        extras = " ".join(
            [
                "{key}={value!r}".format(key=key, value=value)
                for key, value in self._extra.items()
            ]
        )

        return "<{} value={!r} label={!r} order={!r}{extras}>".format(
            self.__class__.__name__,
            self.value,
            self.label,
            self.order,
            extras=" " + extras if extras else "",
        )

    def __getattr__(self, name):
        try:
            return self._extra[name]
        except KeyError:
            raise AttributeError(
                "{!r} object has no attribute {!r}".format(self.__class__, name)
            )


# Shorter convenience alias.
C = ChoiceItem  # noqa


class DjangoChoicesMeta(type):
    """
    Metaclass that writes the choices class.
    """

    name_clean = re.compile(r"_+")

    def __iter__(self):
        for choice in self.choices:
            yield choice

    def __len__(self):
        return len(self.choices)

    def __new__(cls, name, bases, attrs):
        fields = {}
        labels = Labels()
        values = OrderedDict()
        attributes = OrderedDict()
        choices = []

        # Get all the fields from parent classes.
        parents = [b for b in bases if isinstance(b, DjangoChoicesMeta)]
        for kls in parents:
            for field_name in kls._fields:
                fields[field_name] = kls._fields[field_name]

        # Get all the fields from this class.
        for field_name in attrs:
            val = attrs[field_name]
            if isinstance(val, ChoiceItem):
                fields[field_name] = val

        fields = OrderedDict(sorted(fields.items(), key=lambda x: x[1].order))

        for field_name in fields:
            val = fields[field_name]
            if isinstance(val, ChoiceItem):
                if val.label is not None:
                    label = val.label
                else:
                    # TODO: mark translatable by default?
                    label = cls.name_clean.sub(" ", field_name)

                val0 = label if val.value is sentinel else val.value
                choices.append((val0, label))
                attrs[field_name] = StaticProp(val0)
                setattr(labels, field_name, label)
                values[val0] = label
                attributes[val0] = field_name
            else:
                choices.append((field_name, val.choices))

        attrs["choices"] = StaticProp(tuple(choices))
        attrs["labels"] = labels
        attrs["values"] = values
        attrs["_fields"] = fields
        attrs["validator"] = ChoicesValidator(values)
        attrs["attributes"] = Attributes(attributes, fields)

        return super(DjangoChoicesMeta, cls).__new__(cls, name, bases, attrs)


@deconstructible
class ChoicesValidator(object):
    def __init__(self, values):
        self.values = values

    def __call__(self, value):
        if value not in self.values:
            raise ValidationError(
                "Select a valid choice. %s is not "
                "one of the available choices." % value
            )

    def __eq__(self, other):
        return isinstance(other, ChoicesValidator) and self.values == other.values

    def __ne__(self, other):
        return not (self == other)


class DjangoChoices(six.with_metaclass(DjangoChoicesMeta)):
    order = 0
    choices = ()
    labels = Labels()
    values = {}
    validator = None

    @classmethod
    def get_choice(cls, value):
        """
        Return the underlying :class:`ChoiceItem` for a given value.
        """
        attribute_for_value = cls.attributes[value]
        return cls._fields[attribute_for_value]

    @classmethod
    def get_order_expression(cls, field_name):
        """
        Build the Case/When to annotate objects with the choice item order

        Useful if choices represent some access-control mechanism, for example.

        Usage::

        >>> order = MyChoices.get_order_expression('some_field')
        >>> queryset = Model.objects.annotate(some_field_order=order)
        >>> for item in queryset:
        ...     print(item.some_field)
        ...     print(item.some_field_order)
        # first_choice
        # 1
        # second_choice
        # 2
        """
        whens = []
        for choice_item in cls._fields.values():
            whens.append(
                When(
                    **{field_name: choice_item.value, "then": Value(choice_item.order)}
                )
            )
        return Case(*whens, output_field=IntegerField())
