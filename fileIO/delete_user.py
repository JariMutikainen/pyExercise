# define a function delete_users(), which deletes the specified user from the
# users3.csv file. The return value is the number of users removed.
# Like so:
#delete_users("Grace", "Hopper") # Users deleted: 1.
#delete_users("Colt", "Steele") # Users deleted: 2.
#delete_users("Not", "Here") # Users deleted: 0.

def delete_users(first, last):
    deleted_names = 0
    with open('users3.csv', 'r') as fp:
        names = fp.readlines()
        names = [name[:-1] for name in names]  # strip trailing '\n' 
        if not names[-1]:
            names.pop() # Remove the last 'empty element'.
        for name in names:
            if name:
                fname, lname = name.split(',')
                if (fname, lname) == (first, last):
                    names.remove(name)
                    deleted_names += 1

    with open('koe.txt', 'w') as fp:
        for name in names:
            fp.write(name + '\n')

    return 'Users deleted: {}.'.format(deleted_names)


# Testing
#print(delete_users("Grace", "Hopper")) # Users deleted: 1.
print(delete_users("Colt", "Steele")) # Users deleted: 2.
#print(delete_users("Not", "Here")) # Users deleted: 0.

