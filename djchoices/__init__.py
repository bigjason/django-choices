from __future__ import absolute_import, unicode_literals

from pkg_resources import get_distribution

from djchoices.choices import ChoiceItem, DjangoChoices, C

__version__ = get_distribution('django-choices').version

__all__ = ["ChoiceItem", "DjangoChoices", "C"]
