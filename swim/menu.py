# This program uses the classes defined in the file database.py and
# implements a menu like interface for working with the SwimDataBase

from database import Record, SwimDataBase

def import_data_from_disk(dbase):
    # Populate the internal list using the existing data on the disk.
    with open(dbase.filename, 'r') as fp:
        for line in fp:
            date, time, weight = line.split(',')
            dbase.db.append(Record(date, time, weight[:-1])) # Strip '\n'

def export_data_into_disk(dbase):
    with open(dbase.filename, 'w') as fp:
        for record in dbase.db:
            d = record.date
            t = record.time
            w = record.weight
            fp.write(f'{d},{t},{w}\n')

def add_records(dbase):
    ''' Ask user for data, convert it into a Record and append it into the
        tail of the database
    '''
    with open(dbase.filename, 'a') as fp:
        year = '2011'
        answ = 'Overwrite me.'
        # An empty input string will terminate the program.
        while True:
            answ = input('Use format 20 12 4 43 87.4 ----> ')
            if answ:
                day, month, minutes, seconds, kilos = answ.split()
            else:
                break
            date = day + '.' + month + '.' + year
            time = '4' + minutes + ':' + seconds
            dbase.db.append(Record(date, time, kilos))


d1 = SwimDataBase('swim_data.csv')
import_data_from_disk(d1)
#d1.db.append(Record('20.12.2011', '44:03', '88.5'))
#d1.db.append(Record('27.12.2011', '43:03', '90.5'))
#export_data_into_disk(d1)
#print(d1)
#add_records(d1)
#print(d1.db)


