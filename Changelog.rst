=========
Changelog
=========

Unreleased
----------

* Add support for Django 4.1 & 4.2
* Drop support for Django 1.11, 2.2, 3.0, 3.1 (EOL)
* Drop support for Python 2.7, 3.4, 3.5, 3.6, 3.7 (EOL)

1.7.2 (2021-07-12)
------------------

CI maintenance release. There are no actual Python code changes in this release.

* Added explicit support for Django 3.1 and 3.2
* Added explicit support for Python 3.8 and 3.9
* Migrated from Travis CI to Github Actions
* Added Black as code formatter
* Dropped Python 3.4 support since it's not available on Github Actions.

1.7.1 (2019-12-08)
------------------

* Added support for Django 3.0
* Added dependency on non-vendored six

1.7.0 (2019-05-02)
------------------

* Added ``DjangoChoices.get_order_expression`` class method
* Added support for Python 3.7 and Django 2.2
* Dropped support for Django 1.8, Django 1.9 and Django 1.10

1.6.2 (2019-01-24)
------------------

* documentation code blocks are now syntax highlighted (@bashu in #55)
* ``DjangoChoices`` subclasses are now directly iterable (yielding the choice
  tuples) (@brianjbuck in #53)
* documentation of ``DjangoChoices.labels`` is fixed (#54)
* typo fixed in docs (@nielznl in #57)

1.6.0
-----

* Added support for custom attributes to ``ChoiceItem``.
* Added ``DjangoChoices.get_choice`` as public API to retrieve a ``ChoiceItem``
  instance.

See the docs for example usage.

1.5.1
-----

* Fixed inability to set custom order to 0 (#50), thanks to @kavdev for the
  patch and @robinramael for the report
* Added API to get the attribute name from a value (#48), thanks to @jaseemabid
  for the report

1.5.0
-----

* Dropped support for old Python/Django versions.
* Added support for ``NullBooleanField`` -- thanks to @ashwch
* Added retention of choices order in ``DjangoChoices.values`` -- thanks to @merwok

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
