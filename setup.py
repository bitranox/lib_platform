"""Setuptools entry point."""
import codecs
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

description = 'some small helpers used in many scripts'

dirname = os.path.dirname(__file__)
readme_filename = os.path.join(dirname, 'README.rst')
changes_filename = os.path.join(dirname, 'CHANGES.rst')

long_description = description
if os.path.exists(readme_filename):
    try:
        readme_content = codecs.open(readme_filename, encoding='utf-8').read()
        long_description = readme_content
    except Exception:
        pass

if os.path.exists(changes_filename):
    try:
        changes_content = codecs.open(changes_filename, encoding='utf-8').read()
        long_description = '\n'.join((long_description, changes_content))
    except Exception:
        pass

setup(
    name='lib_platform',
    version='1.0.3',
    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Robert Nowotny',
    author_email='rnowotny1966@gmail.com',
    url='https://github.com/bitranox/lib_platform',
    packages=['lib_platform'],
    install_requires=['pytest',
                      'typing',
                      'lib_registry'],
    classifiers=CLASSIFIERS,
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'dill'])
