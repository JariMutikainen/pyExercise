# Write a function copy_and_reverse(), which takes in one text file and
# copies the text of it in reverse into the output file.
#
# copy_and_reverse('story.txt', 'story_reversed.txt')

def copy_and_reverse(in_fname, out_fname):
    o_fpointer = open(out_fname, 'w')
    i_fpointer = open(in_fname, 'r')
    text = i_fpointer.read()
    txet = text[::-1] # reverse the input string (= the contents of input file)
    o_fpointer.write(txet)

    i_fpointer.close()
    o_fpointer.close()


# Testing
copy_and_reverse('story.txt', 'story_reversed.txt')

