#!/usr/bin/env python3

__author__ = 'paolo'

# Here are all of the methods of list objects:

'''
-   list.append(x) Add an item to the end of the list; equivalent to 
    a[len(a):] = [x].
    
-   list.extend(L) Extend the list by appending all the items in the given list;
    equivalent to a[len(a):] = L.

-   list.insert(i, x) Insert an item at a given position. The first argument
    is the index of the element before which to insert, so a.insert(0, x)
    inserts at the front of the list, and a.insert(len(a), x) is equivalent to
    a.append(x).
    
-   list.remove(x) Remove the first item from the list whose value is x.
    It is an error if there is no such item.
'''
#   use of the append() method

a = [1,2,3,4,5]
b = [6,7,8]
a.append(b)
print(a)

#   Use of the .extend() method:

a.extend(b)
print(a)

#   Use of the .append() method

a.append(2)
print(a)

#   Use of .remove() method
a.remove(2)
print(a)


'''
-   list.pop([i]) Remove the item at the given position in the list, and return
    it. If no index is specified, a.pop() removes and returns the last item in
    the list. (The square brackets around the i in the method signature denote
    that the parameter is optional, not that you should type square brackets at
    that position. You will see this notation frequently in the Python Library
    Reference.)
    
-   list.index(x) Return the index in the list of the first item whose value is
     x. It is an error if there is no such item.

-   list.count(x) Return the number of times x appears in the list.

-   list.sort(cmp=None, key=None, reverse=False)
    Sort the items of the list in place (the arguments can be used for sort
    customization, see sorted() for their explanation).
    
-   list.reverse() Reverse the elements of the list, in place.
'''

# Use of .pop() method
print(a)
a.pop(1)
print(a)
a.pop()
print(a)

# use of .reverse() and .sort() methods

a=['a','b','c','d','e']
a.reverse()
print(a)
b=sorted(a)
print(b)
a.sort()
print(a)

'''
    Using Lists as Stacks
'''
''' Stack: the last element added is the first element retrieved (last-in, first-out).'''

stack = [1,2,3]
stack.append(4)
stack.append(5)
stack.append(6)
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

'''
    Using Lists as Queues
'''

''' It is also possible to use a list as a queue, where the first element added
    is the first element retrieved (first-in, first-out).
    Lists are not efficient for this purpose. While appends and pops from the
    end of the list are fast, doing inserts or pops from the beginning of a list
    is slow (because all of the other elements have to be shifted by one).
'''

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.pop(0)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

'''
    To implement a queue, use collections.deque which was designed to have fast
    appends and pops from both ends:
'''

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

'''
    List Comprehensions
'''

'''
-   List comprehensions provide a concise way to create lists. Common
    applications are to make new lists where each element is the result of
    some operations applied to each member of another sequence or iterable,
    or to create a subsequence of those elements that satisfy a certain
    condition.
    
-   For example, assume we want to create a list of squares, like:
'''

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# We can calculate the list of squares using:

square = [x**2 for x in range(10)]

'''
-   A list comprehension consists of brackets containing an expression followed
    by a for clause, then zero or more for or if clauses. The result will be a
    new list resulting from evaluating the expression in the context of the for
    and if clauses which follow it. For example, this listcomp combines the
    elements of two lists if they are not equal:
'''

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(combs)

# and it’s equivalent to:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
