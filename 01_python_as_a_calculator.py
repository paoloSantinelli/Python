#!/usr/bin/env python3
#
__author__ = 'paolo'

def main():
    str = 'stringa di prova'
    num = 10.3
    num1 = 20

    print(str)
    print(num)

    str = '''\
        Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect t0
    '''
    print(str)

    str1 = str.upper()
    print(str1)

if __name__ == "__main__":
    main()