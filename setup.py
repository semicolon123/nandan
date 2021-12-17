#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (ImportError, IOError):
    long_description = open('README.md').read()

setup(
    name='nandan',
    version='0.0.1',
    description=(
        'Stopwords filter for Hindi'
    ),
    long_description=long_description,
    author='Swati Rajwal',
    author_email='rajwalswati213@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'stopword': ['*.txt']},
    platforms=["all"],
    url='https://github.com/semicolon123/nandan',
    download_url='https://github.com/semicolon123/nandan/archive/refs/tags/0.0.1.tar.gz',
    classifiers=[
	'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    zip_safe=True,
)
