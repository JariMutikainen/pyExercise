# Converts a number between 1-7 into a day of the week.
def return_day(num):
    """ Converts a number between 1-7 into a day of the week. """
    days = {
        '1' : 'Sunday',
        '2' : 'Monday',
        '3' : 'Tuesday',
        '4' : 'Wednesday',
        '5' : 'Thursday',
        '6' : 'Friday',
        '7' : 'Saturday'
    }
    return days.get(str(num))

print(return_day(3))
print(return_day(9))
print(return_day.__doc__)
