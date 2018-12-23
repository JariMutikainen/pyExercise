# Write a function, which extracts sequences of eigth '1':s and '0' -
# (i.e. bytes) from the input string. It returns a list of the found
# bytes.
# Example: parse_bytes('Hui hai 10101111 heppa 00001110') ->
#          ['10101111', '00001110']

import re

def parse_bytes(istring):
    # regexp object
    ro = re.compile(r'\b([01]{8})\b')
    return ro.findall(istring)

# Testing
print(parse_bytes('Hui hai 10101111 heppa 00001110')) 
