#!/usr/bin/env python

#
#It is for copy a list of files
#

import os
import sys

if len(sys.argv) != 3:
    sys.exit('Usage: ./clp.py list target_path')

list_path = sys.argv[1]
target_path = sys.argv[2]

import shutil

list = open(list_path,'r')

for path in list.readlines():
    path = path.strip('\n')
    try:
        shutil.copy(path, target_path)
    except IOError:
        sys.stderr.write('Failed: '+path+'\n')

