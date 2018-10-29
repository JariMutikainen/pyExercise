# This file contains the functions needed for 
#    A. Removing an item from the beginning or end of a list and
#    B. Adding an item to the beginning or into the end of a list.
#
# The following examples demonstrate the use of these functions.
#
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") #  1
# list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
def remove_item(i_list,position = 'end'):
    """Removes (and returns) an item from the begining or end of the i_list."""
    if position == 'beginning':
        print(f"Removing {i_list[0]} from {i_list}")
        return i_list.pop(0)
    elif position == 'end':
        print(f"Removing {i_list[-1]} from {i_list}")
        return i_list.pop(-1)
    else:
        print("Illegal argument to remove_item.")
        return

# last = remove_item([1,2,3],'beginning')
# print(last)

def add_item(i_list,position,value):
    """Adds the given value into the beginning or end of the given list and
       returns the new list."""
    if position == 'beginning':
        print(f"Adding {value} into the {position} of {i_list}.")   
        i_list.insert(0,value)
    elif position == 'end':
        print(f"Adding {value} into the {position} of {i_list}.")   
        i_list.append(value)
    else:
        print("Illegal argument to add_item.")
    return i_list


# new_list = add_item([1,2,3],'end',16)
# print(new_list)

def list_manipulation(i_list,action,position,value = 777):
    if action == 'add':
        return add_item(i_list,position,value)
    elif action == 'remove':
        return remove_item(i_list,position)
    else:
        print("Illegal action for the list manipulation.")
        return None

# Testing
print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]

