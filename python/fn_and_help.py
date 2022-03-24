# help is used to understand functions
help(round)


def least_difference(a, b, c):
    """Returns the smallest difference between any two numbers among a, b, and c

    >>> least_difference(1, 5, -6)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),  # trailing commas are allowed in python
)

help(least_difference)

# functions that don't return result in None
mystery = print()
print(mystery)

# default arguments
print(1, 2, 3, sep=' < ')
print(1, 2, 3)


def greet(who="Colin"):
    print("Hello,", who)


greet()
greet(who="Kaggle")
greet("world")


# functions applied to functions
def mult_by_five(x):
    return 5 * x


def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)


def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))


print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', # '\n' is the newline character - it starts a new line
)

