import re

__all__ = ["ChoiceItem", "ChoicesBase", "C"]

class ChoiceItem(object):
    """
    Describes a choice item.  The label is usually the field name so label can
    normally be left blank.  Set a label if you need characters that are illegal
    in a python identifier name (ie: "DVD/Movie"). 
    """
    order = 0
    def __init__(self, value, label=None, order=None):
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
    
    *NOTE*: Does not support inheritance currently.
    """
    name_clean = re.compile(r"_+")
    def __new__(cls, name, bases, attrs):
        class StaticProp(object):
            def __init__(self, value):
                self.value = value
            def __get__(self, obj, objtype):
                return self.value

        sorted_names = []
        for name in attrs:
            if hasattr(attrs[name], "order"):
                sorted_names.append(name)

        sorted_names.sort(key=lambda b: attrs[b].order)

        choices = []
        for name in sorted_names:
            val = attrs[name]
            if isinstance(val, ChoiceItem):
                if val.label:
                    label = val.label
                else:
                    label = cls.name_clean.sub(" ", name)
                choices.append((val.value, label))
                attrs[name] = StaticProp(val.value)
            else:
                choices.append((name, val.choices))

        attrs["choices"] = StaticProp(tuple(choices))

        return super(DjangoChoicesMeta, cls).__new__(cls, name, bases, attrs)

class DjangoChoices(object):
    order = 0
    choices = ()
    __metaclass__ = DjangoChoicesMeta

