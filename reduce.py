#!/usr/bin/env python
import os
import sys
import getopt

def main(argv):
    help_output = "Usage: reduce.py <file> <code> <initial>"
    err_output = help_output

    if len(argv) != 3:
        print err_output
        sys.exit(1)
    
    path = argv[0]
    code = argv[1]
    initial = argv[2]
    ifile = open(path, 'r')
    
    accum = initial
    for line in ifile.readlines():
        accum = eval_code(code, line, accum)

    print accum
    ifile.close()

def eval_code(code, line, accum):
    return eval(code, {'accum':accum, 'line':line.rstrip('\n'), 'path':os.path})

if __name__ == "__main__":
    main(sys.argv[1:])
