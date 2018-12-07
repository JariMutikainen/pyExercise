# Another decorator exercise. The decorator only_ints() must return
# "Please only invoke with integers." in case some of the arguments is
# not an integer. Otherwise it must execute the input function normally.
# 
# @only_ints
# def add(x, y):
    # return x + y
# 
# add(1, 2) # 3
# add("1", "2") # "Please only invoke with integers."
from functools import wraps

def only_ints(fn):
    wraps(fn)
    def wrapper(*argv, **kwargv):
        if not all(type(item) == int for item in argv):
            return "Please only invoke with integers."
        return fn(*argv, **kwargv)
    return wrapper


# Testing

@only_ints
def add(x, y):
    return x + y

print(add(1, 2)) # 3
print(add("1", "2")) # "Please only invoke with integers."

