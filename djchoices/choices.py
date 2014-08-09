import re
from django.utils.datastructures import SortedDict as OrderedDict
from django.core.exceptions import ValidationError

try:
    from django.utils import six
except ImportError:
    import six

__all__ = ["ChoiceItem", "DjangoChoices", "C"]

### Support Functionality (Not part of public API ###

class Labels(dict):
    def __getattribute__(self, name):
        result = dict.get(self, name, None)
        if result is not None:
            return result
        else:
            raise AttributeError("Label for field %s was not found." % name)
    def __setattr__(self, name, value):
        self[name] = value

### End Support Functionality ###

class ChoiceItem(object):
    """
    Describes a choice item.  The label is usually the field name so label can
    normally be left blank.  Set a label if you need characters that are illegal
    in a python identifier name (ie: "DVD/Movie"). 
    """
    order = 0
    def __init__(self, value=None, label=None, order=None):
        self.value = value
        if order:
            self.order = order
        else:
            ChoiceItem.order += 1
            self.order = ChoiceItem.order 
        self.label = label

# Shorter convenience alias.
C = ChoiceItem
        
class DjangoChoicesMeta(type):
    """
    Metaclass that writes the choices class.
    """
    name_clean = re.compile(r"_+")
    def __new__(cls, name, bases, attrs):
        class StaticProp(object):
            def __init__(self, value):
                self.value = value
            def __get__(self, obj, objtype):
                return self.value
                
        fields = {}
        labels = Labels()
        values = {}
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
                if not val.label is None:
                    label = val.label
                else:
                    label = cls.name_clean.sub(" ", field_name)
                choices.append((val.value or label, label))
                attrs[field_name] = StaticProp(val.value or label)
                setattr(labels, field_name, label)
                values[val.value or label] = label
            else:
                choices.append((field_name, val.choices))

        attrs["choices"] = StaticProp(tuple(choices))
        attrs["labels"] = labels
        attrs["values"] = values
        attrs["_fields"] = fields

        return super(DjangoChoicesMeta, cls).__new__(cls, name, bases, attrs)

class DjangoChoices(six.with_metaclass(DjangoChoicesMeta)):
    order = 0
    choices = ()
    labels = Labels()
    values = {}

    @classmethod
    def validator(cls, value):
        if value not in cls.values:
            raise ValidationError('Select a valid choice. %(value)s is not '
                                  'one of the available choices.')

