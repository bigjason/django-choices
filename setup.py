from os import path

from setuptools import find_packages, setup

with open(path.join(path.dirname(__file__), "README.rst")) as f:
    readme = f.read()

setup(
    name="django-choices",
    version="1.7.2",
    license="MIT",
    description="Sanity for the django choices functionality.",
    long_description=readme,
    install_requires=["Django>=1.11", "six>=1.13.0"],
    test_suite="runtests.get_suite",
    url="https://github.com/bigjason/django-choices",
    author="Jason Webb",
    author_email="bigjasonwebb@gmail.com,sergeimaertens@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
