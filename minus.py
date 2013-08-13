#!/usr/bin/env python

#
#

import os
import sys

if len(sys.argv) != 4:
    sys.exit('Usage: ./minus.py minuend subtrahend result_file')

minuend = open(sys.argv[1],'r')
subtrahend = open(sys.argv[2],'r')
result = open(sys.argv[3],'w')

exist_set = set(subtrahend.readlines())

for line in minuend.readlines():
    if not line in exist_set:
        result.write(line)

result.close()
subtrahend.close()
minuend.close()
        
