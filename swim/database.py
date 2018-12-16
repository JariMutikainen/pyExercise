# This program appends new data into the tail of the file swim_data.csv
# The data has to be entered manually using an improvised short hand writing
# style. To append the following line into the swim_data.csv:
#
# 20.12.2011,44:43,87.4
#
# enter the following string at the prompt:
#
# 20 12 4 43 87.4
#
# To quit the program enter an empty string instead.

class Record:
    '''
    A record in the SwimDataBase consists of 3 string-type fields':
    date: The date of the session, 
    time: The time spent on swimming 2km with the free style stroke,
    weight: The weight of the swimmer.
    
    Usage: r1 = Record('15.12.2018', '43:07', '90.4')

    '''
    def __init__(self, date, time, weight):
        self.date = date # A string
        self.time = time # A string
        self.weight = weight # A string
        self._mins, self._secs = self.time.split(':')
        self.minutes = int(self._mins)
        self.seconds = int(self._secs)
        self.kilos = float(self.weight)

    def __repr__(self):
        return f'({self.date}, {self.time}, {self.weight}kg)'

class SwimDataBase:
    '''
    A SwimDataBase consists of Records. Each Record contains the
    data of one swimming session. The existing data is kept on
    the disk in a .csv file, but it is read into an internal list
    when an instance of the SwimDataBase class is created.

    Usage: db = SwimDataBase('swim_data.csv')

    '''
    def __init__(self, filename):
        self.filename = filename
        self.db = [] # The elements of this list are of the class Record.

    def __repr__(self):
        self.s1 = f'SwimDataBase stored in the file "{self.filename}"' 
        self.s2 = f' consists of {len(self.db)} records.'
        return self.s1 + self.s2





#r1 = Record('15.12.2018', '43:07', '90.4')
#print(r1)
#print(r1.minutes, r1.seconds, r1.weight)
#db = SwimDataBase('swim_data.csv')
#print(db)
#help(SwimDataBase)
#
