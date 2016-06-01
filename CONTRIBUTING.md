# Contributing

Open source projects shine when anyone can contribute, and this project is no different. However, there are some guidelines
to adhere to in order to get your contribution merged in. In general, if you adhere to the Django contributing
guidelines, all is well: https://docs.djangoproject.com/en/dev/internals/contributing/

First, fork the repository and then clone it:

  git glone git@github.com:your-username/django-choices.git

Make sure you have Django installed (a virtualenv is recommended), and the test dependencies:

  pip install Django tox

## Tests

All changes should be accompanied by a test that either tests the new behaviour, or tests the regression.
Make sure all the tests still pass after your changes - for your current Django and Python version this
can be done by running:

  python runtests.py

And to run the entire matrix of Django and tox versions:

  tox

## Documentation

When behaviour changes or gets added, check whether the documentation needs updates. If so, please
submit a draft or final version.

## Pull requests

When you think the patch is ready, submit a pull request to the `develop` branch. If it's a bug fix,
the maintainer(s) will take care of bumping the version and uploading to PyPI. Feel free to add
yourself to the CONTRIBUTORS.md file.

## Smaller style guidelines

### Commit(s)

Try to keep commits as atomic as possible. It's fine to do many small commits before submitting the PR,
you can always rebase your branch to make a nice commit history. A commit that adds the test, and
then a different commit that fixes the issue/feature is reasonable, combining them is fine as well.

### Code style

* Stick to PEP8, with the exclusion of the 80-char max line length. 80 columns is a guideline, 120 is the
  upper limit.
* Use 4 spaces instead of tabs.
* Follow https://docs.djangoproject.com/en/1.9/internals/contributing/writing-code/coding-style/
