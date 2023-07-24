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
    install_requires=["Django>=3.2", "six>=1.13.0"],
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
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
