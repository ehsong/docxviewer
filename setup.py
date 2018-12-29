#!/usr/bin/env python3

from setuptools import setup, find_packages


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='docxviewer',
    version='0.0.4',
    description='Tool for previewing multiple .docx files in a directory',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ehsong/docviewer',
    author=['Eunhou Esther Song'],
    author_email='eunhou.song@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
    install_requires=required,
    entry_points={
        'console_scripts': ['docxviewer = docxviewer.doc_viewer:main']
    }
    )
