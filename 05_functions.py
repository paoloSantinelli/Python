#!/usr/bin/env python3

__author__ = 'paolo'

#   Defining Functions

'''
-   The keyword "def" introduces a function definition. It must be followed by the
    function name and the parenthesized list of formal parameters.
    The statements that form the body of the function start at the next line, and
    must be indented.
'''
'''
-   The first statement of a functinon body can optionally be a string literal;
    this string literal is the function's documentation string, or docstring.
'''

def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

'''
-   The actual parameters (arguments) to a function call are introduced in the
    local symbol table of the called function when it is called; thus, arguments
    are passed using call by value (where the value is always an object reference,
    not the value of the object).
    When a function calls another function, a new local symbol table is created
    for that call.
'''

# Now call the function we just defined:
fib(2000)

'''
-   A function definition introduces the function name in the current symbol table.
    The value of the function name has a type that is recognized by the interpreter
    as a user-defined function.
    This value can be assigned to another name which can then also be used as a
    function. This serves as a general renaming mechanism:
'''

f=fib
print(f(5))

'''
-   Return statement. The functions without a return statement do return a value,
    albeit a rather boring one. This value is called "None" (it's a built-in name).
    Writing the value None is normally suppressed by the interpreter if it would
    be the only value written. It can be shown by using print:
'''

fib(0)
print(fib(0))

'''
-   fib2(n) is a function that returns a list of the numbers of the Fibonacci
    series:
'''

def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # Equivalent expression(but not as efficient as):
        a, b = b, a+b       # result = result + [a]
    return result

fib2(100)

f100 = fib2(100)
f100

'''
-   Functions with a variable number of arguments.

    There are three forms, which can be combined:
        a) Default Argument Values;
        b) Keyword Arguments;
        c) Arbitrary Argument Lists;
'''

'''
a)  Default Argument Values
    The most useful form is to specify a default value for one or more arguments.
    This creates a function that can be called with fewer arguments than it is
    defined to allow. For example:
'''

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print(complaint)

' The function can be called in several ways: '

' giving only the mandatory argument: ask_ok("Do you really want to quit?") '
' giving one of the optional arguments: ask_ok("OK to overwrite the file?", 2) '
' giving all arguments: ask_ok("OK to overwrite the file?", 2, "Come on, only yes or no!")'

'''
-   This function introduces the in keyword. This tests whether or not a sequence
    contains a certain value.
'''


'''
-   The default values are evaluated at the point of function definition in the
    defining scope, so that
'''

i = 5

def f(arg = i):
    print(arg)

i = 6
f()

' will print 5'

'''
-   Important warning: The default value is evaluated only once. This makes a
    difference when the default is a mutable object such as a list, dictionary,
    or instances of most classes. For example, the following function
    accumulates the arguments passed to it on subsequent calls:

-   The following function accumulates the arguments passed to it on subsequent
    calls:
'''

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

'''
-   If you don't want the default to be shared between subsequent calls,
    you can write the function like this instead:
'''

def f(a, L=None):
    if L == None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


'''
b)  Keyword Arguments:
    Functions can also be called using keyword arguments of the form kwarg=value.
    For instance, the following function:
'''

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action)
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

''' This function accepts one required argument (voltage), and three optional
    arguments (state, action, type).
    This function can be called in any of the following ways:
'''
'''
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
'''

'''
    but all the following calls would be invalid:

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
'''

'''
-   In a function call, keyword arguments must follow positional arguments.
    All the keyword arguments passed must match one of the arguments
    accepted by the function (e.g. actor is not a valid argument for the parrot
    function), and their order is not important. This also includes non-optional
    arguments (e.g. parrot(voltage=1000) is valid too).
'''

'''
c)  Arbitrary Argument Lists
    The least frequently used option is to specify that a function can be called
    with an arbitrary number of arguments.
    These arguments will be wrapped up in a tuple (see Tuples and Sequences).
    Before the variable number of arguments, zero or more normal arguments may
    occur. In the same fashion, dictionaries can deliver keyword arguments with
    the **-operator.
'''

'   arbitrary number of arguments wrapped in a tuple:'

def multiple_args(primo, *args):
    print(primo)
    for arg in args:
        print(arg)

multiple_args('nome', 1,2,3,4,5,6,'cognome')

#   end of example

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

fp=open('data.txt', 'w')
write_multiple_items(fp, ',', 'nome', 'cognome', 'citta', 'via')


'   Dictionaries can deliver keyword arguments with the **-operator:'

def keyword_arguments(primo, **kargs):
    print(primo)
    for key in kargs:
        print(key, kargs[key])

keyword_arguments(123, nome='paolo', cognome='Santinelli', eta=15)

