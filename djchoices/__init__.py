import os
from distutils.version import StrictVersion

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    v = StrictVersion(f.readlines()[0])
    VERSION = v.version
    __version__ = str(v)

from djchoices.choices import ChoiceItem, DjangoChoices, C

__all__ = ["ChoiceItem", "DjangoChoices", "C"]
