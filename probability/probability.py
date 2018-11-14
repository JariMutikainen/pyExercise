# Consider the following game:
# There are 3 doors. Behind one of them there is a new car. Behind the two
# other doors there is not. If a contestant is able to guess correctly where
# the car is he can have the car as a prize.
#
# Assume, that the contestant selects one of the 3 doors. The door is not
# opened immediately. Instead the host of the contest opens one of the
# remaining other two doors. If the car is behind the door selected by the
# host the contestant will not get the prize: nobody wins.
# However, if the space behind the host's door is empty
# the contestant is given an opportunity to either stick to the door he
# originally selected or to change his mind and choose the other remaining
# closed door. What should he do to maximize his odds of winning the new car?
#
# To make the experiment we imagine two players with opposite tactics:
#
#   Aleksi always takes the opportunity to change his mind.
#
#   Jari always sticks to his original selection.
#
# Let's see who wins more often.

from random import randint
# When the following constant is set to True, the host knows, 
# where the car is, and he will always select a door with no
# car behind it.
HOST_KNOWS = False  
host_wins = 0
jari_wins = 0
aleksi_wins = 0
for i in range(100000):
    doors = ['Empty', 'Empty', 'Empty']
    # randint(0,2) returns a random number r so that 0 <= r <= 2
    doors[randint(0, 2)] = 'Car'  # Place the car behind one of the 3 doors.
    # print(doors)

    jaris_selection = randint(0, 2)  # The player makes his original selection
    # Initialize to the same as Jari's choice:
    hosts_selection = jaris_selection
    if HOST_KNOWS:
        # The host selects one of the two remaing doors with no car behind it. 
        # This is accomplished by re-selecting until such a door is 'found'.
        while ( (hosts_selection == jaris_selection) or
                (doors[hosts_selection] == 'Car')):
            # Keep moving until a door with no car behind it is 'found'.
            hosts_selection = (hosts_selection + 1) % 3 # resulting range: 0-2
    else:
        # Host doesn't know, where the car is. He selects at random
        # one of the two doors, which Jari did not select.
        while hosts_selection == jaris_selection:
            hosts_selection = randint(0, 2)
    # Aleksi is left with the door, which has been selected neither by Jari
    # nor the host.
    aleksis_selection = jaris_selection  # Initialize to the same as Jari's.
    # Keep moving until the last unselected door is found.
    while (     (aleksis_selection == jaris_selection) or
                (aleksis_selection == hosts_selection)):
        # Try 0,1,2 until found.
        aleksis_selection = (aleksis_selection + 1) % 3
    ostring = f"Jari's selection = {jaris_selection}" + "\n"
    ostring += f"Host's selection = {hosts_selection}" + "\n"
    ostring += f"Aleksi's selection = {aleksis_selection}"
    # print(ostring)
    if doors[hosts_selection] == 'Car':
        host_wins += 1
        # print("Host wins. Nobody gets the car.")
    elif doors[jaris_selection] == 'Car':
        jari_wins += 1
        # print("Jari wins. Jari gets the car.")
    elif doors[aleksis_selection] == 'Car':
        aleksi_wins += 1
        # print("Aleksi wins. Aleksi gets the car.")
    else:
        # print("Something is WRONG. Find out what")
        pass
print(f"Jari won {jari_wins} times.")
print(f"Aleksi won {aleksi_wins} times.")
print(f"The host won {host_wins} times.")
