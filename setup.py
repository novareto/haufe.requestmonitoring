# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import sys

version = '0.6.2.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
])

install_requires = [
    'setuptools',
    'Zope2',
    'zope.processlifetime',
]

setup(
    name='haufe.requestmonitoring',
    version=version,
    description="Zope 2 request monitoring",
    long_description=long_description,
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.2",
        "Framework :: Zope2",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Logging",
    ],
    keywords='zope long-running-request monitor logging',
    author='Haufe-Lexware',
    author_email='info@zopyx.com',
    maintainer='Andreas Jung',
    maintainer_email='info@zopyx.com',
    license='ZPL',
    url='http://github.com/collective/haufe.requestmonitoring',
    packages=find_packages(),
    namespace_packages=['haufe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""
    # -*- Entry points: -*-
    """,
)
