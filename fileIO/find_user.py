# Write a function find_user(), which takes in a first name a nd a last name.
# If a person with that name exists in the file users.csv the function returns
# the corresponding line number of the .csv-file. Otherwise the message
# 'not found' is returned instead. Like so:
#
#find_user("Colt", "Steele") # 1
#find_user("Alan", "Turing") # 3
#find_user("Not", "Here") # 'Not Here not found.'

from csv import reader

def find_user(first_name, last_name):
    with open('users.csv') as fp:
        line_iterable = reader(fp)
        for row_number, name in enumerate(line_iterable):
            if [first_name, last_name] == name:
                return row_number
    return first_name + ' ' + last_name + ' not found.'



# Testing
print(find_user("Colt", "Steele")) # 1
print(find_user("Alan", "Turing")) # 3
print(find_user("Not", "Here")) # 'Not Here not found.'

