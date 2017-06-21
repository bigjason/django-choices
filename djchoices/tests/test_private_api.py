import unittest

from djchoices import C, ChoiceItem, DjangoChoices  # noqa


class PrivateAPITests(unittest.TestCase):

    def test_labels_dict(self):
        """
        Ref #33: IPython reads the Labels.keys() for pretty printing.
        """
        class Choices(DjangoChoices):
            a = ChoiceItem('a', 'A')
            b = ChoiceItem('b', 'B')

        self.assertEqual(Choices.labels.a, 'A')
        self.assertEqual(Choices.labels.b, 'B')
        with self.assertRaises(AttributeError):
            Choices.labels.c

        keys = Choices.labels.keys()
        self.assertEqual(set(keys), set(['a', 'b']))
