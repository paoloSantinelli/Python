#!/usr/bin/env python3

__author__ = 'paolo'

def main():
    #   if statemants

    x = int(input("Please enter an integer: "))

    if x < 0:
        x = 0
        print("Negative changed to zero")

    elif x == 0:
        print("Zero")

    elif x == 1:
        print("Uno")

    else:
        print ("More")

#**************************************************
#   for statements
#   Python's for statement iterates over the items
#   of any sequence (a list or a string),
#   in the order that they appear in the sequence

    words = ['cane', 'gatto', 'giraffa', 'zebra']
    for w in words:
        print(w, len(w))

# iterate over a copy of the sequence:

    words = ['cane', 'gatto', 'giraffa', 'zebra']

    for w in words[:]:
        words.insert(0,w)
        print(words)


# The range() function generates a list of arithmetic progression:

    print(range(10))

# To iterate over the indices of a sequence, range() and len() can be combined as flollows:

    a = ['Mary', 'had', 'a', 'little', 'lamb']

    for i in range(len(a)):
        print(i, a[i])

# The position index and the corresponding value can be retrieved at the same time using the
# enumerate function()

    for i, v in enumerate(a):
        print(i, v)

# Break, Continue statements and else Clauses on loop

# The break statement, breaks out of the smallest enclosing for or while loop.

# Code fragments to search for the prime numbers

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n/x)
                break
            elif(x == n-1):
            # loop fell through without finding a factor
                print(n, 'is a prime number')


# The continue statements continues with the next iteration of the loop:

    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)

# The pass statements do nothing

class MyEmptyClass:     # An empty class
    pass

if __name__ == '__main__':
    main()
