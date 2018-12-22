# Write a function is_valid_time(), which returns True if the input
# string represents time. Otherwise return False.
# Examples:
#'20:33' -> True
# '1:00' -> True
# '2:2' -> False
# 
# Note: '88:07' -> True.
# Concentrate on format. No need to verify the values.

import re
def is_valid_time(tstring):
    ro = re.compile(r'^\d{1,2}:\d{2}$') # regexp object
    mo = ro.search(tstring) # match object
    return bool(mo)

# Testing
print(is_valid_time('22:30')) # True
print(is_valid_time('2:38')) # True
print(is_valid_time('2:8')) # False
print(is_valid_time('134')) # False
