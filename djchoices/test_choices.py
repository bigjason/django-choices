import unittest

from djchoices import DjangoChoices, C, ChoiceItem

class NumericTestClass(DjangoChoices):
    Item_1 = C(1)
    Item_2 = C(2)
    Item_3 = C(3)

class DjangoChoices(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_numeric_class_values(self):
        self.assertEqual(NumericTestClass.Item_1, 1)
        self.assertEqual(NumericTestClass.Item_2, 2)
        self.assertEqual(NumericTestClass.Item_3, 3)
        
    def test_numeric_class_order(self):
        choices = NumericTestClass.choices
        self.assertEqual(choices[0][0], 1)
        self.assertEqual(choices[1][0], 2)
        self.assertEqual(choices[2][0], 3)
    