import unittest

from django.db.models import TextChoices

from djchoices import ChoiceItem, DjangoChoices


class ToMigrate(DjangoChoices):
    option_1 = ChoiceItem("option_1")
    option_2 = ChoiceItem("option_2", "Option 2")


class Native(TextChoices):
    option_1 = "option_1", "option 1"
    option_2 = "option_2", "Option 2"


class NativeChoicesEquivalenceTests(unittest.TestCase):
    def test_labels(self):
        labels = ToMigrate.labels
        native = dict(zip(Native.names, Native.labels))

        self.assertEqual(native, labels)

    def test_values(self):
        values = ToMigrate.values
        native = dict(zip(Native.values, Native.labels))

        self.assertEqual(native, values)

    def test_attributes(self):
        attributes = ToMigrate.attributes
        native = dict(zip(Native.values, Native.names))

        self.assertEqual(native, attributes)

    def test_get_choice(self):
        a_choice = ToMigrate.get_choice(ToMigrate.option_2)
        native = Native[Native.option_2]

        self.assertEqual(native.value, a_choice.value)
        self.assertEqual(native.label, a_choice.label)
