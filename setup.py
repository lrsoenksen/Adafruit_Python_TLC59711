#!/usr/bin/env python

from distutils.core import setup

setup(name            = "adafruit_tlc59711",
      version         = "1.0.0",
      description     = "Python library to control Adafruit TLC59711 boards",
      requires        = ['spidev'],
      author          = "Tony DiCola and modified by Luis Soenksen",
      author_email    = "tony@tonydicola.com",
      maintainer      = "Luis Soenksen",
      maintainer_email= "soenksen@mit.edu",
      license         = "MIT",
      url             = "https://github.com/lrsoenksen/Adafruit_Python_TLC59711",
      py_modules      = ['adafruit_tlc59711'],
)
