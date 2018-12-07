# Make a python decorator, which ensures, that only an authorised person
# is able to run a given program. One of the key word arguments has to as
# follows:
#
# key : 'role'
# value: 'admin'
# 
# @ensure_authorized
# def show_secrets(*args, **kwargs):
#       return "Shh! Don't tell anybody!"
# 
# show_secrets(role="admin") # "Shh! Don't tell anybody!"
# show_secrets(role="nobody") # "Unauthorized"
# show_secrets(a="b") # "Unauthorized"

from functools import wraps

def ensure_authorized(fn):
    wraps(fn)
    def wrapper(*args, **kwargs):
        if any(k == 'role' and v == 'admin' for k, v in kwargs.items()):
            return fn(*args, **kwargs)
        return 'Unauthorized'
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

# Testing

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"
print(show_secrets(a="b")) # "Unauthorized"
