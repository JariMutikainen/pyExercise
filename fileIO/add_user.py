# Make a function add_user(), which takes in a first name and a last name
# and append them into an existing .csv-file users.csv like so:
# add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson

# THIS PROGRAM DOES NOT WORK IN WINDOWS PROPERLY. IT ADDS AN EXTRA CHARACTER
# '^M' INTO THE END OF LINE.

from csv import writer

def add_user(first_name, last_name):
    with open('users.csv', 'a', newline='') as f:
        csv_writer = writer(f)
        csv_writer.writerow([first_name, last_name])


# Testing
add_user('Teemu', 'Selanne')
add_user('Mickey', 'Mouse')
add_user('Donald', 'Duck')

