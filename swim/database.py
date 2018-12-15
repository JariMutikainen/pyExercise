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
    '''
    def __init__(self, date, time, weight):
        self.date = date
        self.time = time
        self.weight = weight

    def __repr__(self):
        return self.date + ', ' + self.time + ', ' + self.weight + 'kg'

class SwimDataBase:
    '''
    A SwimDataBase consists of Records. Each Record contains the
    data of one swimming session. The existing data is kept on
    the disk in a .csv file, but it is read into an internal list
    when an instance of the SwimDataBase class is created.
    '''
    def __init__(self, filename):
        self.filename = filename
        self.db = []

    def __repr__(self):
        self.s1 = f'SwimDataBase stored in the file "{self.filename}"' 
        self.s2 = f' consists of {len(self.db)} records.'
        return self.s1 + self.s2


#with open('swim_data.csv', 'a') as fp:
    #year = '2011'
    #answ = 'Overwrite me.'
    ## An empty input string will terminate the program.
    #while True:
        #answ = input('Use format 20 12 4 43 87.4 ----> ')
        #if answ:
            #day, month, minutes, seconds, kilos = answ.split()
        #else:
            #break
        #date = day + '.' + month + '.' + year
        #time = '4' + minutes + ':' + seconds
        #fp.write(date + ',' + time + ',' + kilos + '\n')

r1 = Record('15.12.2018', '43:07', '90.4')
print(r1)
db = SwimDataBase('swim_data.csv')
print(db)
help(SwimDataBase)

