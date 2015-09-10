from os import path
from setuptools import setup, find_packages


with open(path.join(path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name="django-choices",
    version='1.4.2',
    license="MIT",
    description="Sanity for the django choices functionality.",
    long_description=readme,
    install_requires=['Django>=1.3', 'six'],
    test_suite='runtests.get_suite',
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
       "Framework :: Django",
       "Programming Language :: Python :: 2.6",
       "Programming Language :: Python :: 2.7",
       "Programming Language :: Python :: 3.3",
       "Programming Language :: Python :: 3.4",
       "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
