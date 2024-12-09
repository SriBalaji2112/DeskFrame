#!/usr/bin/env python3
# https://github.com/SriBalaji2112/voice_identification

import io
import os
import re
from setuptools import setup, find_packages

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

# Find version info from module (without importing the module):
# with open('voice_identification/__init__.py', 'r') as fd:
#     version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
#                         fd.read(), re.MULTILINE).group(1)

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

setup(
    name='deskframe',
    version="v1.0.1",
    url='https://github.com/SriBalaji2112/DeskFrame/',
    author='BalajiSanthanam',
    author_email='sribalaji2112@gmail.com',
    description=('DeskFrame is a Python library that simplifies the process of creating graphical user interfaces '
                 '(GUIs) using XML for layout design and Python for backend logic. '),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD 3-Clause License',
    packages=find_packages(),
    package_data={'deskframe': ['deskframe.exe']},
    entry_points={
            'console_scripts': [
                'deskframe=deskframe.deskframe:main',
            ],
        },
    install_requires=[
        'pymsgbox',
        'pytweening>=1.0.4',
        'pyscreeze>=0.1.21',
        'pygetwindow>=0.0.5',
        'customtkinter',
        'Pillow',
        'tkinter_webcam',
        'plyer'],
    keywords="GUI tkinter customtkinter ctk tk python application network api ui gui deskframe app desktop create gui",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)