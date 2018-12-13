# Make a function print_users(), which assumes that a 'users.csv'-file
# exists in the current directory, and the function prints out all the
# names in that file.
from csv import reader

def print_users():
    with open('users.csv') as fp:
        csv_reader = reader(fp)
        next(csv_reader) # Skip the 1st line = the header
        for line in csv_reader:
            print('{} {}'.format(line[0], line[1]))

# Testing
print_users()
