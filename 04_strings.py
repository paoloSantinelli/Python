#!/usr/bin/env python3

__author__ = 'paolo'

def main():

    print('single   quotes string')
    print("double   quotes string")  # single or double quotes act the same way
    print('Use backslashes to escape quotes or \' special characters')
    print("You can use signel quotes '' inside a double quotes string")
    print('Or double quotes "" inside single quotes string')

# Multiple lines string
    print('''\
    This is a multiple lines string example:

    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
    ''')

    '''
    multiline comment
    If you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings
    by adding an r before the first quote:
    '''

    # raw string
    print('C:\some\name')

    print(R'C:\some\name')

    print(r'C:\some\name')

    # Strings concatenation, (glued together) with the + operator, and repeated with *:

    print(3 * 'un' + 'imu')

    str = 'Cat'
    print(str + 'white')

    # String indexing

    str = 'Python'
    print(str[0])
    print(str[5])
    print(str[-1])  # Last character

    # String slicing

    print(str[1:5]) # Characters from position 1 (included) to position 5 (excluded)

    print(str[:4])  # an omitted first index default to 0

    print(str[2:])  # an omitted second index default to the size of the string

    print(str[-2:]) # Characters frim the second last to the end

    # Python strings cannot be changed -- they are immutable.
    # Therefore, assigning to an indexed position in the string results in an error:

    str[0] = 'I'

    # The built-in function len() returns the length of a string:

    s = 'The quick brown fox jumps over the lazy dog'

    len(s)

    # For string methods see:
    # https://docs.python.org/3.9/library/stdtypes.html#string-methods

if __name__ == "__main__":
    main()