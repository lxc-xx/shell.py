#!/usr/bin/env python

import os
import sys

def main(argv):
    if len(argv) != 1:
        print("Usage: tree.py <path>")
        sys.exit(1)
    path = argv[0]

def explore(path, depth, pres):
    basename = os.path.basename(path)
    
    d = depth - 1
    line = ''
    
    floor = True
    while d >= 0:
        if pres[d] <= 0:
            if floor:
                line.append('_')
            else:
                line.append(' ')
        else:
            line.append('|')
            floor = False
        d -= 1

    line = line[::-1]
    line += '_' + basename

    print line

    pres[depth] -= 1

    if os.isdir(path):
        children = os.listdir(path)
        num = len(children)
        pres.append(num)
        for child in children
            explore(os.path.join(path, child), depth + 1, pres)
        
    if pres[-1] <= 0:
        pres.pop()

    
    
    


    
    




if __name__ == '__main__':
    main(sys.argv[1:])

