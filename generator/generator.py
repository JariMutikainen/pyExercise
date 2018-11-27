# This exercise is about using a generator in Python. The task is to
# make a generator, which yields one weekday at a time starting from
# 'Monday', when called as follows: next(days).

# Define a generator function. It uses 'yield' as opposed to 'return'.
# That is what makes it a generator function.
def week():
    d_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
               'Saturday','Sunday')

    # When the d_tuple has been completely exhausted all the further calls
    # to next() will raise 'StopIteration'-exception.
    for d in d_tuple:
        yield d

# Testing
days = week()
for i in range(10): # go beyond 7 days on purpose to raise some exceptions too.
    try:
        print(next(days))
    except StopIteration:
        print('No more days available.') 

