# The task is to do as follows:
# Input:
#
# names = [{'first': 'Elie', 'last': 'Schoppik'}, 
#          {'first': 'Colt', 'last': 'Steele'}]
#
# The expected output:
#
# extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
def extract_full_name(d_list):
    name_list = []
    for d in d_list:
        name_list.append(d['first'] + ' ' + d['last'])
    return name_list

# Testing:
names = [{'first': 'Elie', 'last': 'Schoppik'}, 
         {'first': 'Colt', 'last': 'Steele'}]

print(extract_full_name(names))

