# This program takes in a list of dates in the format 'MM/DD/YYYY' and returns
# the earliest one of them. The range of MM is 01 - 99 and the range of
# DD is 01 - 99. This piece of unrealism was added to the task to prevent
# people from using the datetime module of python for solving the problem.
# At first the program takes in only two dates, but the final version sould be
# able to process any number of dates.

def get_earliest(*args):
    def date2days(date):
        """
        Converts a date into a number of days since the birth of Jesus.
        """
        month, day, year = date.split('/')
        return int(int(year) * 356 + int(month) * 30.5 + int(day))

    earliest = args[0]
    for date in args:
        if date2days(date) < date2days(earliest):
            earliest = date

    return earliest




# Testing
#date = "01/27/1756"
#print(get_earliest("01/27/1756", "01/27/1802"))
#print(get_earliest("01/27/1802", "01/27/1756", "06/17/1964"))
