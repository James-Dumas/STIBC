#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Simple TI-BASIC Compiler',
    version='1.3',
    description="TI-BASIC Compiler/Decompiler",
    author='James Dumas',
    url='https://github.com/James-Dumas/STIBC',
    license="GNU General Public License",
    packages=['src',],
    scripts=["src/stibc",],
    data_files=[('share/stibc', ['src/tokens.json',],),]
)
