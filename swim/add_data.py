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

with open('swim_data.csv', 'a') as fp:
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
        fp.write(date + ',' + time + ',' + kilos + '\n')
