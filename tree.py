#!/usr/bin/env python

import os
import sys

def main(argv):
    if len(argv) != 1:
        print("Usage: tree.py <path>")
        sys.exit(1)
    path = argv[0]
    path = path.rstrip('/')
    explore(path, -1, [], True)

def explore(path, depth, pres, is_top = False):
    #print pres
    basename = os.path.basename(path)
    is_dir = os.path.isdir(path)

    line_list = [] 
    if not is_top: 
        d = depth 
        is_floor = True 
        while d >= 0: 
            if pres[d] <= 0: 
                if is_floor: 
                    line_list.append('__')
                else:
                    line_list.append('  ')
            else:
                if is_floor and pres[d] == 1:
                    line_list.append(' `')
                else: 
                    line_list.append(' |')
                is_floor = False 
            d -= 1 
        line_list = line_list[::-1] 
        line_list += '--' + basename
        pres[depth] -= 1
        print ''.join(line_list)
    else:
        print basename

    if is_dir:
        children = os.listdir(path) 
        num = len(children) 
        pres.append(num) 
        for child in children: 
            explore(os.path.join(path, child), depth + 1, pres)
        pres.pop()

if __name__ == '__main__':
    main(sys.argv[1:])
