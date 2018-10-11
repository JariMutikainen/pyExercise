# Ask the user for a distance in km and convert that into miles.
print("Enter the distance in km:")
km = input() # input()-function returns a string
miles = float(km) / 1.609
#print(km + " km equals to " + str(miles) + " miles.")
print(f"{km} km equals to {miles} miles.")

