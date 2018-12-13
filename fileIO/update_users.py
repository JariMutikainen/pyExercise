# update_users() takes in old frist name, old last name, new first name
# and new last name. It substitutes the new names for the old ones in the 
# file users2.csv. The return value is the number of names changed.
#
# update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
# update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
# update_users("Not", "Here", "Still not", "Here") # Users updated: 0.

def update_users(old_first, old_last, new_first, new_last):
    with open('users2.csv') as f_in:
        old_names = [item.strip() for item in f_in.readlines()]
        new_names = []
        changed_names = 0
        for name in old_names:
            if name == old_first + ',' + old_last:
                new_names.append(new_first + ',' + new_last + '\n')
                changed_names += 1
            else:
                new_names.append(name + '\n')

    with open('users2.csv', 'w') as f_out:
        f_out.writelines(new_names)

    return 'Users updated: {}.'.format(changed_names)


# Testing
print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.
