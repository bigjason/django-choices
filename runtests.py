try:
    import unittest2 as unittest
except ImportError:
    import unittest

from os import path
from sys import stdout


def get_suite():
    disc_folder = path.abspath(path.dirname(__file__))

    stdout.write("Discovering tests in '%s'..." % disc_folder)
    suite = unittest.TestSuite()
    loader = unittest.loader.defaultTestLoader
    suite.addTest(loader.discover(disc_folder, pattern="test*.py"))
    stdout.write("Done.\n")
    return suite


def run_tests():
    suite = get_suite()
    stdout.write("Running tests...\n")
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(suite.run)


if __name__ == "__main__":
    run_tests()
