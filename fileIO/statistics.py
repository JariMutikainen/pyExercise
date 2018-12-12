# Write a function statistics(), which takes in a file name and returns
# a dictionary of the contents as follows:
# statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}

def statistics(f_name):
    lines = 0
    words = 0
    chars = 0
    with open(f_name) as fp:
        for line in fp:
            lines += 1
            chars += len(line)
            words += len(line.split())
            #print(f'{line}: {len(line)} {len(line.split())}')

    out_dict = {}
    out_dict['lines'] = lines
    out_dict['words'] = words
    out_dict['characters'] = chars
    return out_dict

#Testing
print(statistics('koe.txt'))
#print(statistics('story.txt'))

