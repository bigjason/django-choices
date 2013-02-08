from os import path
from setuptools import setup, find_packages
from distutils.version import StrictVersion

with open(path.join(path.dirname(__file__), 'djchoices/VERSION')) as f:
    VERSION = StrictVersion(f.readlines()[0])

with open(path.join(path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name="django-choices",
    version=str(VERSION),
    license="MIT",
    description="Sanity for the django choices functionality.",
    long_description=readme,
    url="https://github.com/bigjason/django-choices",
    author="Jason Webb",
    author_email="bigjasonwebb@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
       "Development Status :: 5 - Production/Stable",
       "Operating System :: OS Independent",
       "License :: OSI Approved :: MIT License",
       "Intended Audience :: Developers",
       "Programming Language :: Python :: 2.6",
       "Programming Language :: Python :: 2.7"
    ]
)
