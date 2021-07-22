# code golf challenge
# https://code.golf/diamonds#python
# wren 20210701

# Print a size ascending range of Diamonds using the numbers 1 to 9,
# ranging from size 1 to size 9, each diamond separated by a blank line.
#
# A size 1 diamond should look like this, a single centered 1:
#
#          1
# With the largest size 9 diamond looking like this:
#
#          1
#         121
#        12321
#       1234321
#      123454321
#     12345654321
#    1234567654321
#   123456787654321
#  12345678987654321
#   123456787654321
#    1234567654321
#     12345654321
#      123454321
#       1234321
#        12321
#         121
#          1

# https://www.diffchecker.com/diff
# use to check diff between texts for output

# this one makes the diamonds independent of each other
# def make_diamond(size):
#     collect = []
#     for number,space in zip(range(1,size+1),range(size,0,-1)):
#         blank = ' '*space
#          # = [*range(1,11)] # just makes a list of ints in range
#         sequence = ''.join(list(map(str,range(1,number+1))))
#         line = ''.join((blank,sequence,sequence[-2::-1],blank))
#         collect.append(line)
#         print(line)
#     print('\n'.join(collect[-2::-1]))
#     print()

# function to print a diamond
def make_diamond(size):
    # initalize a list to collect the increasing lines, in order to
    # then print this sequence of strings in reverse order
    # for the bottom half of teh diamond
    collect = []
    # for each line in the sizes, begining with 1 and continueing to
    # the desired max central line size of the diamond
    for number in range(1,size+1):
        # make a variable for the blank spaces to print until the
        # string value, which is 10 (to make an even center line for all the
        # diamonds) minus the iterable number being used to make the printed
        # string
        blank = ' '*(10-number)
        # join the sequence of intagers as strings to print, making a list of
        # these by mapping the range of values into a string with map to then be
        # converted to a list and put in the variable sequence
        sequence = ''.join(list(map(str,range(1,number+1))))
        # make the line that is actually printed of teh joined strings
        # begingin with the number of blank spaces, then the sequence of numbers
        # then the sequnce reversed with out the last number to avoid repeating
        # the center value, then the blank number of spaces again
        line = ''.join((blank,sequence,sequence[-2::-1],blank))
        # collect this created line to a list of lines to print in the correct
        # order for the bottom half of the diamond without repeating this loop
        # creating the sequence
        collect.append(line)
        # now print this string sequence on a line
        print(line)
    # from the collected series, print in reverse order excluding the center
    # line which should only be printed once, each in a new line by joining
    # on character \n
    print('\n'.join(collect[-2::-1]))
    # to make sure the first diamond of size 1 prints correctly with only one
    # blank space until the next diamond, add a conditional. I feel like this
    # could be coded implicitly
    if len(collect)>1:
        print()

# make a list of the sizes of the diamonds to make for the requested range
# of sizes, from 1 to 9 (10 for zero based)
sizes = list(range(1,10))
# map the list of sizes to the function that prints the images, minus the
# last item in the list of mappings, which prints none for some reason
list(map(make_diamond,sizes))[-1]
