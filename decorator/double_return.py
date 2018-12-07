# Another decorator exercise. double_return() taakes a function as an input.
# it decorates the function by returning two copies of the inner functions
# return value inside of a list. Like so:
# @double_return
# def add(x, y):
    # return x + y
# 
# add(1, 2) # [3, 3]
# 
# @double_return
# def greet(name):
    # return "Hi, I'm " + name
# 
# greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
from functools import wraps
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        o_list = []
        o_list.append(result)
        o_list.append(result)
        return o_list
    return wrapper

@double_return
def add(x, y):
    return x + y

@double_return
def greet(name):
    return "Hi, I'm " + name

# Testing
print(add(1, 2)) # [3, 3]
print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]
