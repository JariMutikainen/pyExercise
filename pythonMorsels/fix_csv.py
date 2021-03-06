# This week we're going to practice normalizing CSV files. Write a program
# fix_csv.py that turns a pipe-delimited file into a CSV file. I'll
# explain how it should work by example.
# 
# Your original file will look like this:
# 
# Reading|Make|Model|Type|Value
# Reading 0|Toyota|Previa|distance|19.83942
# Reading 1|Dodge|Intrepid|distance|31.28257
# 
# You'll then run your script by typing this at the command line:
# 
# $ python fix_csv.py cars-original.csv cars.csv
# 
# Note : "$" is not typed; that is simply the beginning of the prompt.
# 
# Your fixed file should then look like this:
# 
# Reading,Make,Model,Type,Value
# Reading 0,Toyota,Previa,distance,19.83942
# Reading 1,Dodge,Intrepid,distance,31.28257

from sys import argv
import re

#print(f'{argv[0]}, {argv[1]}, {argv[2]}')
if len(argv) != 3:
    raise BaseException('Use: python fix_csv.py <i_file> <o_file>')

ifile = argv[1]
ofile = argv[2]
with open(ifile) as rfp:
    with open(ofile, 'w') as wfp:
        for iline in rfp:
            oline = re.sub(r'[|]', ',', iline)
            #print(oline, end='')
            wfp.write(oline)



