=========
Changelog
=========

1.5.0
-----

* Dropped support for old Python/Django versions.
* Added support for ``NullBooleanField`` -- thanks to @ashwch

..  warning::
    Dropped support for Python versions < 2.7 and 3.3, and Django < 1.8. If you
    need explicit support for these versions, you should stick to version 1.4.4.

1.4.4
-----

* Bugfix for better IPython support (125d523e1c94e4edb344e3bb3ea1eab6f7d073ed)

1.4.3
-----

Fixed a bug in the validator error message output - thanks to Sobolev Nikita

1.4 to 1.4.1
------------
This is a small release that fixes some ugliness. In Django 1.7 and up, the
validator can now be used as documented in the readme. Before this version, the
error::

    ValueError: Cannot serialize: <bound method DjangoChoicesMeta.validator of <class 'choices.models.MyModel.Choices'>>

would be raised, and a workaround was to define a validator function calling the
choices' validator, requiring everything to be defined in the module scope.

This is now fixed by moving to a class based validator which is deconstructible.


1.3 to 1.4
----------
* Added support for upcoming Django 1.9, by preferring stlib SortedDict over
  Django's OrderedDict
* Added pypy to the build matrix
* Added coverage to the Travis set-up
