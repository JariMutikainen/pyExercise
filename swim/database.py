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

    def import_data_from_disk(self):
        'Populates the internal list using the existing data on the disk.'
        with open(self.filename, 'r') as fp:
            for line in fp:
                date, time, weight = line.split(',')
                self.db.append(Record(date, time, weight[:-1])) # Strip '\n'

    def export_data_into_disk(self):
        '''
        Writes the contents of the internal list into the .csv file
        on the disk.
        '''
        with open(self.filename, 'w') as fp:
            for record in self.db:
                d = record.date
                t = record.time
                w = record.weight
                fp.write(f'{d},{t},{w}\n')

    def show_tail(self, n=1):
        'Prints the last n lines of the internal list. n must be an int.'
        # Can't print more than the size of the list
        lines = min(n,len(self.db)) 
        start = len(self.db) - lines
        stop = len(self.db)
        for n in range(start, stop):
            print(f'{n}: {self.db[n]}')

    def append_new_record(self, item):
        '''Appends a new item of the class Record into the tail of the
         internal list'''
        self.db.append(item)

