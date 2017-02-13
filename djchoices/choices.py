from __future__ import absolute_import, unicode_literals

import re
from collections import OrderedDict

from django.core.exceptions import ValidationError
from django.utils import six
from django.utils.deconstruct import deconstructible


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

    def __init__(self, value=sentinel, label=None, order=None):
        self.value = value
        self.label = label

        if order:
            self.order = order
        else:
            ChoiceItem.order += 1
            self.order = ChoiceItem.order

# Shorter convenience alias.
C = ChoiceItem  # noqa


class DjangoChoicesMeta(type):
    """
    Metaclass that writes the choices class.
    """
    name_clean = re.compile(r"_+")

    def __new__(cls, name, bases, attrs):
        fields = {}
        labels = Labels()
        values = OrderedDict()
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
            else:
                choices.append((field_name, val.choices))

        attrs["choices"] = StaticProp(tuple(choices))
        attrs["labels"] = labels
        attrs["values"] = values
        attrs["_fields"] = fields
        attrs["validator"] = ChoicesValidator(values)

        return super(DjangoChoicesMeta, cls).__new__(cls, name, bases, attrs)


@deconstructible
class ChoicesValidator(object):

    def __init__(self, values):
        self.values = values

    def __call__(self, value):
        if value not in self.values:
            raise ValidationError('Select a valid choice. %s is not '
                                  'one of the available choices.' % value)

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
