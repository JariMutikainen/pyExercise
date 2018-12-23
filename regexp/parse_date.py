# Write a parse_date() function, which takes in a date string. The following
# 3 formats are accepted
# dd/mm/yyyy
# dd.mm.yyyy
# dd,mm,yyyy
#
# The function must return a dictionary with the 'd', 'm' and 'y' as keys
# like so:
# print(parse_date('22.12.2018'))
# {'d': '22', 'm': '12', 'y': '2018'}

import re

def parse_date(date_string):
    # regexp object
    reo = re.compile(
        r'^(?P<d>[0-9]{2})[.,/](?P<m>[0-9]{2})[.,/](?P<y>[0-9]{4})$')
    # match object
    mo = reo.search(date_string)
    if mo:
        return {'d' : mo.group('d'),
                'm' : mo.group('m'),
                'y' : mo.group('y')
                }
    return None


# Testing
print(parse_date('22.12.2018'))
print(parse_date('22,12,2018'))
print(parse_date('22/12/2018'))
print(parse_date('Pekka'))

    
