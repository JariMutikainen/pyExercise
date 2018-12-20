# This program uses the classes defined in the file database.py and
# implements a menu like interface for working with the SwimDataBase

from database import Record, SwimDataBase
from sys import exit

class Menu:
    'Asks the user for desired action and carries it out.'

    def __init__(self):
        self.d1 = SwimDataBase('swim_data.csv')
        self.choices = {
                '1': self.import_data,
                '2': self.show_tail_rows,
                '3': self.add_records,
                '4': self.export_data,
                '5': self.quit
                }

    def display_menu(self):
        'Displays the alternatives for the next action.'
        print('''
            Select one of the following actions:

                1: import_data_from_disk,
                2: show_tail,
                3: add_records,
                4: export_data_into_disk,
                5: quit
                ''')

    def run(self):
        while True:
            'Displays the menu and runs the choices'
            self.display_menu()
            choice = input('Enter your selection: ')
            while choice not in self.choices.keys():
                print('Illegal selection. Try again.')
                self.display_menu()
                choice = input('Enter your selection: ')
            self.choices[choice]() # Adding () calls one of the methods.

    def import_data(self):
        self.d1.import_data_from_disk()
        print(f'Imported statistics data from {self.d1.filename}')

    def show_tail_rows(self):
        num = input('Enter the number of the last records to be shown: ')
        print(f'The last {num} records are as follows:')
        self.d1.show_tail(int(num))
            
    def add_records(self):
        ''' Asks the user for data, converts it into a Record and 
            calls the method append_new_record() to add it into the
            tail of the instance attribute list of the data base.
        '''
        year = '2017'
        answ = 'Overwrite me.'
        # An empty input string will terminate the program.
        while True:
            answ = input('Use format 20 12 4 43 87.4 ----> ')
            if answ:
                try:
                    day, month, minutes, seconds, kilos = answ.split()
                except ValueError:
                    print('Incorrect number of arguments.')
                    print('The input was ignored. Try again.')
            else:
                break
            date = day + '.' + month + '.' + year
            time = '4' + minutes + ':' + seconds
            self.d1.append_new_record(Record(date, time, kilos))

    def export_data(self):
        self.d1.export_data_into_disk()
        print(f'''
            Exported the internal data base into the file {self.d1.filename}
            ''')

    def quit(self):
        print('Thank you for using the SwimDataBase. See you next time.')
        exit(0)

if __name__ == '__main__':
    Menu().run()

    
#d1 = SwimDataBase('swim_data.csv')
#d1.import_data_from_disk()
#d1.db.append(Record('20.12.2011', '44:03', '88.5'))
#d1.db.append(Record('27.12.2011', '43:03', '90.5'))
#d1.export_data_into_disk()
#print(d1)
#add_records(d1)
#print(d1.db)
#d1.show_tail(2)


