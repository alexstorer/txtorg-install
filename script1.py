#!/usr/bin/python2.6

import urllib
import subprocess

import os

print os.getcwd()

import glob

print glob.glob('*')

subprocess.call('sudo easy_install-2.6 JCC-2.8-py2.6-macosx-10.6-universal.egg',shell=True)
subprocess.call('sudo easy_install-2.6 lucene-3.1.0-py2.6-macosx-10.6-universal.egg',shell=True)
