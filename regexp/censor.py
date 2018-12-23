# Write a function censor(), which takes in a string and censores out
# the 'f-word' 'frack' - like so:
#
# censor('Frack you') -> 'CENSORED you'
# censor('I hope you fracking die.') -> 'I hope you CENSORED die.'
# censor('You fracking frack.') -> 'You CENSORED CENSORED.'

import re

def censor(istring):
    regexp_obj = re.compile(r'\b[Ff]rack\S*')
    return regexp_obj.sub('CENSORED',istring)


# Testing
print(censor('Frack you!')) # -> 'CENSORED you'
print(censor('I hope you fracking die.')) # -> 'I hope you CENSORED die.'
print(censor('You fracking frack.')) # -> 'You CENSORED CENSORED.'
