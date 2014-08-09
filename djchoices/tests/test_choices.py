try:
  import unittest2 as unittest
except ImportError:
  import unittest

from djchoices import DjangoChoices, C, ChoiceItem

class NumericTestClass(DjangoChoices):
    Item_1 = C(1)
    Item_2 = C(2)
    Item_3 = C(3)

class StringTestClass(DjangoChoices):
    empty = ChoiceItem("", "")
    One = ChoiceItem("O")
    Two = ChoiceItem("T")
    Three = ChoiceItem("H")

class SubClass1(NumericTestClass):
    Item_4 = C(4)
    Item_5 = C(5)

class SubClass2(SubClass1):
    Item_6 = C(6)
    Item_7 = C(7)

class EmptyValueClass(DjangoChoices):
    Option1 = ChoiceItem()
    Option2 = ChoiceItem()
    Option3 = ChoiceItem()


class DjangoChoices(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numeric_class_values(self):
        self.assertEqual(NumericTestClass.Item_1, 1)
        self.assertEqual(NumericTestClass.Item_2, 2)
        self.assertEqual(NumericTestClass.Item_3, 3)

    def test_class_labels(self):
        self.assertEqual(StringTestClass.labels.empty, "")
        self.assertEqual(NumericTestClass.labels.Item_1, "Item 1")
        self.assertEqual(NumericTestClass.labels.Item_2, "Item 2")
        self.assertEqual(NumericTestClass.labels.Item_3, "Item 3")

    def test_class_labels_inherited(self):
        self.assertEqual(SubClass2.labels.Item_2, "Item 2")
        self.assertEqual(SubClass2.labels.Item_6, "Item 6")

    def test_class_values(self):
        self.assertEqual(SubClass1.values[SubClass1.Item_1], "Item 1")
        self.assertEqual(SubClass1.values[SubClass1.Item_4], "Item 4")
        self.assertEqual(SubClass1.values[SubClass1.Item_5], "Item 5")

    def test_numeric_class_order(self):
        choices = NumericTestClass.choices
        self.assertEqual(choices[0][0], 1)
        self.assertEqual(choices[1][0], 2)
        self.assertEqual(choices[2][0], 3)

    def test_string_class_values(self):
        self.assertEqual(StringTestClass.One, "O")
        self.assertEqual(StringTestClass.Two, "T")
        self.assertEqual(StringTestClass.Three, "H")

    def test_string_class_order(self):
        choices = StringTestClass.choices
        self.assertEqual(choices[0][0], "")
        self.assertEqual(choices[1][0], "O")
        self.assertEqual(choices[2][0], "T")
        self.assertEqual(choices[3][0], "H")

    def test_sub_class_level_1_choices(self):
        choices = SubClass1.choices
        self.assertEqual(choices[0][0], 1)
        self.assertEqual(choices[3][0], 4)
        self.assertEqual(choices[4][0], 5)

    def test_sub_class_level_1_values(self):
        self.assertEqual(SubClass1.Item_1, 1)
        self.assertEqual(SubClass1.Item_4, 4)
        self.assertEqual(SubClass1.Item_5, 5)

    def test_sub_class_level_2_choices(self):
        choices = SubClass2.choices
        self.assertEqual(choices[0][0], 1)
        self.assertEqual(choices[3][0], 4)
        self.assertEqual(choices[5][0], 6)
        self.assertEqual(choices[6][0], 7)

    def test_sub_class_level_2_values(self):
        self.assertEqual(SubClass2.Item_1, 1)
        self.assertEqual(SubClass2.Item_5, 5)
        self.assertEqual(SubClass2.Item_6, 6)
        self.assertEqual(SubClass2.Item_7, 7)

    def test_sub_class_name(self):
        self.assertEqual(NumericTestClass.__name__, "NumericTestClass")
        self.assertEqual(SubClass2.__name__, "SubClass2")

    def test_numeric_class_validator(self):
        from django.core.exceptions import ValidationError

        self.assertEqual(None, NumericTestClass.validator(1))
        self.assertEqual(None, NumericTestClass.validator(2))
        self.assertEqual(None, NumericTestClass.validator(3))

        self.assertRaises(ValidationError, NumericTestClass.validator, 0)
        self.assertRaises(ValidationError, NumericTestClass.validator, 4)
        self.assertRaises(ValidationError, NumericTestClass.validator, 5)
        self.assertRaises(ValidationError, NumericTestClass.validator, 6)
        self.assertRaises(ValidationError, NumericTestClass.validator, 7)

    def test_subclass1_validator(self):
        from django.core.exceptions import ValidationError

        self.assertEqual(None, SubClass1.validator(1))
        self.assertEqual(None, SubClass1.validator(2))
        self.assertEqual(None, SubClass1.validator(3))
        self.assertEqual(None, SubClass1.validator(4))
        self.assertEqual(None, SubClass1.validator(5))

        self.assertRaises(ValidationError, SubClass1.validator, 0)
        self.assertRaises(ValidationError, SubClass1.validator, 6)
        self.assertRaises(ValidationError, SubClass1.validator, 7)

    def test_subclass_2_validator(self):
        from django.core.exceptions import ValidationError

        self.assertEqual(None, SubClass2.validator(1))
        self.assertEqual(None, SubClass2.validator(2))
        self.assertEqual(None, SubClass2.validator(3))
        self.assertEqual(None, SubClass2.validator(4))
        self.assertEqual(None, SubClass2.validator(5))
        self.assertEqual(None, SubClass2.validator(6))
        self.assertEqual(None, SubClass2.validator(7))

        self.assertRaises(ValidationError, SubClass2.validator, 0)
        self.assertRaises(ValidationError, SubClass2.validator, 8)

    def test_empty_value_class(self):
        choices = EmptyValueClass.choices
        self.assertEqual(choices[0][0], "Option1")
        self.assertEqual(choices[1][0], "Option2")
        self.assertEqual(choices[2][0], "Option3")
