try:
    import unittest2 as unittest
except ImportError:
    import unittest

from os import path
from sys import stdout


if __name__ == "__main__":
    disc_folder = path.abspath(path.dirname(__file__))

    stdout.write("Discovering tests in '%s'..." % disc_folder)
    suite = unittest.TestSuite()
    loader = unittest.loader.defaultTestLoader
    suite.addTest(loader.discover(disc_folder, pattern="test*.py"))
    stdout.write("Done.\n")

    stdout.write("Running tests...\n")
    runner = unittest.TextTestRunner()
    runner.verbosity = 2
    runner.run(suite.run)
