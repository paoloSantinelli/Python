#!/usr/bin/env python3
#
__author__ = 'paolo'

import sys
import os


def main():
    print('The command line arguments are:')
    a=0
    for i in sys.argv:
        print (i)
        a=a+1

    print('Argomenti = '+ str(a))
    print('Current directory : '+os.getcwd()+'\n\n')
    print('\n\nThe PYTHONPATH is', sys.path, '\n')

if __name__ == "__main__":
    main()