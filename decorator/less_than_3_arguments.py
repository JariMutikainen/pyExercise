# Make a decorator, which ensures that a decorated function has less than 3
# positional arguments. In case of more arguments than that return
# "Too many arguments!". Examples:
# @ensure_fewer_than_three_args
# def add_all(*nums):
    # return sum(nums)
# 
# add_all() # 0
# add_all(1) # 1
# add_all(1,2) # 3
# add_all(1,2,3) # "Too many arguments!"
# add_all(1,2,3,4,5,6) # "Too many arguments!"

from functools import wraps

def ensure_fewer_than_three_args(fn):
    wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        else:
            return fn(*args, **kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

# Testing
print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"
