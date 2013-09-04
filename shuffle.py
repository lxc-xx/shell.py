#!/usr/bin/env python
import sys
import random

def main(argv):
    file_name = argv[0]

    f = open(file_name, 'r')
    lines = f.readlines()
    random.shuffle(lines)

    for line in lines:
        print line.rstrip('\n')

    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: shuffle.py file"
        sys.exit(1)

    main(sys.argv[1:])
