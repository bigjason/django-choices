import unittest

from django.db.models import Case, IntegerField, Value, When

from djchoices import C, ChoiceItem, DjangoChoices


class NumericTestClass(DjangoChoices):
    Item_0 = C(0)
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


class NullBooleanValueClass(DjangoChoices):
    Option1 = ChoiceItem(None, "Pending")
    Option2 = ChoiceItem(True, "Successful")
    Option3 = ChoiceItem(False, "Failed")


class DuplicateValuesClass(DjangoChoices):
    Option1 = ChoiceItem("a")
    Option2 = ChoiceItem("a")


class OrderedChoices(DjangoChoices):
    Option1 = ChoiceItem("a", order=1)
    Option2 = ChoiceItem("b", order=0)


class ExtraAttributeChoices(DjangoChoices):
    Option1 = ChoiceItem(0, help_text="Option1 help text")
    Option2 = ChoiceItem(
        1, help_text="Option2 help text", validator_class_name="RegexValidator"
    )


class DjangoChoices(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numeric_class_values(self):
        self.assertEqual(NumericTestClass.Item_0, 0)
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

    def test_class_values_order(self):
        self.assertEqual(list(StringTestClass.values), ["", "O", "T", "H"])

    def test_numeric_class_order(self):
        choices = NumericTestClass.choices
        self.assertEqual(choices[0][0], 0)
        self.assertEqual(choices[1][0], 1)
        self.assertEqual(choices[2][0], 2)
        self.assertEqual(choices[3][0], 3)

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
        self.assertEqual(choices[0][0], 0)
        self.assertEqual(choices[4][0], 4)
        self.assertEqual(choices[5][0], 5)

    def test_sub_class_level_1_values(self):
        self.assertEqual(SubClass1.Item_1, 1)
        self.assertEqual(SubClass1.Item_4, 4)
        self.assertEqual(SubClass1.Item_5, 5)

    def test_sub_class_level_2_choices(self):
        choices = SubClass2.choices
        self.assertEqual(choices[0][0], 0)
        self.assertEqual(choices[4][0], 4)
        self.assertEqual(choices[6][0], 6)
        self.assertEqual(choices[7][0], 7)

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

        self.assertRaises(ValidationError, NumericTestClass.validator, 4)
        self.assertRaises(ValidationError, NumericTestClass.validator, 5)
        self.assertRaises(ValidationError, NumericTestClass.validator, 6)
        self.assertRaises(ValidationError, NumericTestClass.validator, 7)

    def test_validation_error_message(self):
        from django.core.exceptions import ValidationError

        message = "Select a valid choice. 4 is not " "one of the available choices."

        self.assertRaisesRegexp(ValidationError, message, NumericTestClass.validator, 4)

    def test_subclass1_validator(self):
        from django.core.exceptions import ValidationError

        self.assertEqual(None, SubClass1.validator(1))
        self.assertEqual(None, SubClass1.validator(2))
        self.assertEqual(None, SubClass1.validator(3))
        self.assertEqual(None, SubClass1.validator(4))
        self.assertEqual(None, SubClass1.validator(5))

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

        self.assertRaises(ValidationError, SubClass2.validator, 8)

    def test_empty_value_class(self):
        choices = EmptyValueClass.choices
        self.assertEqual(choices[0][0], "Option1")
        self.assertEqual(choices[1][0], "Option2")
        self.assertEqual(choices[2][0], "Option3")

    def test_null_boolean_value_class(self):
        choices = NullBooleanValueClass.choices
        self.assertEqual(choices[0][0], None)
        self.assertEqual(choices[1][0], True)
        self.assertEqual(choices[2][0], False)
        self.assertEqual(choices[0][1], "Pending")
        self.assertEqual(choices[1][1], "Successful")
        self.assertEqual(choices[2][1], "Failed")

    def test_deconstructible_validator(self):
        deconstructed = NumericTestClass.validator.deconstruct()
        self.assertEqual(
            deconstructed,
            ("djchoices.choices.ChoicesValidator", (NumericTestClass.values,), {}),
        )

    def test_attribute_from_value(self):
        attributes = NumericTestClass.attributes
        self.assertEqual(attributes[0], "Item_0")
        self.assertEqual(attributes[1], "Item_1")
        self.assertEqual(attributes[2], "Item_2")
        self.assertEqual(attributes[3], "Item_3")

    def test_attribute_from_value_duplicates(self):
        with self.assertRaises(ValueError):
            DuplicateValuesClass.attributes

    def test_choice_item_order(self):
        choices = OrderedChoices.choices
        self.assertEqual(choices[0][0], "b")
        self.assertEqual(choices[1][0], "a")

    def test_get_choices(self):
        choices_class = NullBooleanValueClass

        self.assertEqual("Pending", choices_class.get_choice(None).label)
        self.assertEqual("Successful", choices_class.get_choice(True).label)
        self.assertEqual("Failed", choices_class.get_choice(False).label)

    def test_get_extra_attributes(self):
        choices_class = ExtraAttributeChoices

        self.assertEqual(
            "Option1 help text",
            choices_class.get_choice(choices_class.Option1).help_text,
        )

        self.assertEqual(
            "Option2 help text",
            choices_class.get_choice(choices_class.Option2).help_text,
        )

        self.assertEqual(
            "RegexValidator",
            choices_class.get_choice(choices_class.Option2).validator_class_name,
        )

    def test_get_extra_attributes_unknown_attribute_throws_error(self):
        choices_class = ExtraAttributeChoices

        with self.assertRaises(AttributeError):
            choices_class.get_choice(choices_class.Option1).unknown_attribute

    def test_repr(self):
        choices_class = ExtraAttributeChoices
        repr_string = repr(choices_class.get_choice(choices_class.Option2))

        self.assertIn("<ChoiceItem value=1 label=None order=22", repr_string)
        self.assertIn("validator_class_name='RegexValidator'", repr_string)
        self.assertIn("help_text='Option2 help text'", repr_string)

    def test_iteration(self):
        """
        If this test fails it will raise:
        `TypeError: 'DjangoChoicesMeta' object is not iterable`
        """
        for _ in StringTestClass:
            pass

    def test_choices_len(self):
        self.assertEqual(len(StringTestClass), 4)

    def test_order_annotation(self):
        case = OrderedChoices.get_order_expression("dummy")

        expected = Case(
            When(dummy="b", then=Value(0)),
            When(dummy="a", then=Value(1)),
            output_field=IntegerField(),
        )

        self.assertEqual(repr(case), repr(expected))
