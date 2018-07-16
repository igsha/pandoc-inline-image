#!/usr/bin/env python

from setuptools import setup
import re

script = 'pandoc-inline-image'
script_content = open(script).read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", script_content))

setup(
    name=script,
    version=metadata['version'],
    description=metadata['description'],
    url="https://github.com/igsha/pandoc-inline-image",
    author="igsha",
    license="LICENSE",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Text Processing"
    ],
    scripts=[script],
    install_requires=['panflute >= 1.10.6'],
)
