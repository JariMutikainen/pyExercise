# This is an exercise of writing and using a decorator function in python.
# show_args() takes a function in as an argument. It prints the arguments
# of that function and then calls the function itself. See below:
# 
# @show_args
# def do_nothing(*args, **kwargs):
    # pass
# 
# do_nothing(1, 2, 3,a="hi",b="bye")
# 
# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}

from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print('Here are the args: ', args)
        print('Here are the kwargs: ', kwargs)
        return fn(*args, **kwargs)
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    """
    I'm a dummy function, which does nothing.
    """
    print('\nExecuting nothing now. My 1st argument is {}.'.format(args[0]))

# Testing
print(do_nothing.__doc__)
#help(do_nothing)
do_nothing(1, 2, 3,a="hi",b="bye")

