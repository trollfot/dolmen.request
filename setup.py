# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__),'docs',*rnames)).read()
 
def test_read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), 
                'src', 'dolmen', 'request' ,*rnames)).read()

version = '0.1'
long_description = (read('README.txt') + '\n' +
                    '.. contents::\n\n' + 
                    read('HISTORY.txt') + '\n' +
                    test_read('test_overview.txt'))

install_requires = [
    'cromlech.browser >= 0.4',
    'cromlech.dawnlight',
    'cromlech.io >= 0.2a1',
    'grokcore.component >= 2.1',
    'martian >= 0.13',
    'setuptools',
    'zope.component',
    ]

tests_require = [
    'cromlech.browser [test]'
    ]

setup(
    name='dolmen.request',
    version=version,
    author='Grok & Dolmen Teams',
    author_email='dolmen@list.dolmen-project.org',
    url='http://gitweb.dolmen-project.org',
    description='Grok-like configuration for View components',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['dolmen'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        },
    )
