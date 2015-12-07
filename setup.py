#!/usr/bin/env python

from os.path import dirname, join
from pip.req import parse_requirements
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import domain_squeezer
import sys

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read_file(*pathname):
    return open(join(dirname(__file__), *pathname)).read()


def read_requirements():
    filepath = join(dirname(__file__), 'requirements.txt')
    generator = parse_requirements(filepath, session=False)
    return [str(requirement.req) for requirement in generator]


setup(
    name='django-domain-squeezer',
    version=domain_squeezer.__version__,
    author=domain_squeezer.__author__,
    author_email=domain_squeezer.__author_email__,
    maintainer=domain_squeezer.__maintainer__,
    maintainer_email=domain_squeezer.__maintainer_email__,
    url=domain_squeezer.__url__,
    license=domain_squeezer.__license__,

    description=domain_squeezer.__doc__.strip(),
    long_description=read_file('README.rst'),
    keywords='domains, monetization, django, python',

    classifiers=CLASSIFIERS,
    install_requires=read_requirements(),
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    zip_safe=False,

    tests_require=['pytest', 'tox'],
    cmdclass={'test': PyTest},
)
