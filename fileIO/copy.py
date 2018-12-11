# Write a program, which copies all the lines from one text fie into another
# text file.

def copy(r_file_name, w_file_name):
    # r_file = open(r_file_name)
    w_file = open(w_file_name,'w')
    with open(r_file_name) as r_file:
        for line in r_file:
            w_file.write(line)
    w_file.close()

# Testing
copy('story.txt', 'story_copy.txt')
