# This program converts the swim_data.csv file into a SQLite3 data base.
import sqlite3
#infile = 'sample.csv'
infile = 'swim_data.csv'

# Open a connection to an existing data base or 
# create a new one it it doesn't exist yet.
conn = sqlite3.connect('swim_data.db') 
# Create a cursor object
c = conn.cursor()
# Create a new table. 
c.execute('CREATE TABLE swim_table (date TEXT, time TEXT, weight TEXT)')
with open(infile) as csv_file:
    for line in csv_file:
        line = line.strip() # Strip off the trailing '\n'
        date, time, weight = line.split(',')
        query = 'INSERT INTO swim_table VALUES (?,?,?)'
        c.execute(query, (date, time, weight))

# Commit changes from the internal memory into the db on the disk
conn.commit()
# Always remember to close the connection at the end!
conn.close()

