# This is an exercise about using keyword arguments to a function.
#
# This is how the function should work:
#
# calculate(make_float=False, operation='add', message='You just added', 
#           first=2, second=4) # "You just added 6"
# calculate(make_float=True, operation='divide', first=3.5, second=5) 
#           # "The result is 0.7"

def calculate(**kwargs):
    """
    This function accepts key word arguments as an input. It performs
    the requested calculation and adds the requested comment string to the 
    output.
    """
#    print(kwargs)
    op = kwargs['operation']
    a = kwargs['first']
    b = kwargs['second']
    msg = "The result is"
    res = 0
    if 'message' in kwargs.keys():
        msg = kwargs['message']     # Overwrite the default message.
    if op == 'add':
        res = a + b
    elif op == 'subtract':
        res = a - b
    elif op == 'multiply':
        res = a * b
    elif op == 'divide':
        res = a / b
    else:
        print("Illegal operation type {}".format(kwargs['operation']))
    if kwargs['make_float']:
        res = float(res)
    else:
        res = int(res)

    print(msg + " " + str(res))
    return msg + " " + str(res)

# Testing:
calculate(make_float=False, operation='add', message='You just added', 
          first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) 
        # "The result is 0.7"

