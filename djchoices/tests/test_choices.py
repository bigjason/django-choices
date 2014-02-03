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

class PluralLabelTestClass(DjangoChoices):
    apple = ChoiceItem("a", label="Apple", label_plural="Apples")
    box = ChoiceItem("b", label="Box", label_plural="Boxes")


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

    def test_class_default_plural_labels(self):
        self.assertEqual(StringTestClass.labels_plural.empty, "")
        self.assertEqual(NumericTestClass.labels_plural.Item_1, "Item 1")
        self.assertEqual(NumericTestClass.labels_plural.Item_2, "Item 2")
        self.assertEqual(NumericTestClass.labels_plural.Item_3, "Item 3")

    def test_class_plural_labels(self):
        self.assertEqual(PluralLabelTestClass.labels.apple, "Apple")
        self.assertEqual(PluralLabelTestClass.labels_plural.apple, "Apples")
        self.assertEqual(PluralLabelTestClass.labels.box, "Box")
        self.assertEqual(PluralLabelTestClass.labels_plural.box, "Boxes")

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
