#!/usr/bin/python
# coding=utf-8
from distutils.core import setup

__author__ = "Aleksandr Shyshatsky"

setup(name='GameParams.data helper for World of Warships',
      version='1.0',
      description='Utility that simplifies work with GameParams.data file from World of Warships game',
      author=__author__,
      author_email='shalal545@gmail.com',
      url='https://github.com/Monstrofil/game_params_wows',
      packages=['game_params_util'],
      py_modules=['GameParams'],
      scripts=['game_params.py'],
      )
