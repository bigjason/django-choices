"""
Module to handle different Django/Python version libraries.
"""
try:
    from collections import OrderedDict
except ImportError:  # Py2.6, fall back to Django's implementation
    from django.utils.datastructures import SortedDict as OrderedDict  # pragma: no cover


try:
    from django.utils import six
except ImportError:
    import six  # pragma: no cover


try:
    from django.utils.deconstruct import deconstructible
except ImportError:
    # just return a noop decorator
    def deconstructible(cls):
        return cls
