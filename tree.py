#!/usr/bin/env python

import os
import sys

def main(argv):
    if len(argv) != 1:
        print("Usage: tree.py <path>")
        sys.exit(1)
    path = argv[0]
    path = path.rstrip('/')
    explore(path, 0, [1])

def explore(path, depth, pres):
    basename = os.path.basename(path)
    is_dir = os.path.isdir(path)
    
    d = depth
    line_list = []
    
    is_floor = True
    while d >= 0:
        if pres[d] <= 0: 
            if is_floor: 
                line_list.append('__')
            else:
                line_list.append('  ')
        else:
            line_list.append(' |')
            is_floor = False
        d -= 1

    line_list = line_list[::-1] 
    line_list += '_' + basename
    
    print ''.join(line_list)

    pres[depth] -= 1

    if is_dir:
        children = os.listdir(path) 
        num = len(children) 
        pres.append(num) 
        for child in children: 
            explore(os.path.join(path, child), depth + 1, pres)
        pres.pop()

if __name__ == '__main__':
    main(sys.argv[1:])
