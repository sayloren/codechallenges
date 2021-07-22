# code golf challenge
# https://code.golf/christmas-trees#python
# wren 20210621

# Print a size ascending range of Christmas trees using asterisks, ranging from size 3 to size 9, each tree separated by a blank line.
#
# A size 3 tree should look like this, with a single centered asterisk for the trunk:
#
#    *
#   ***
#  *****
#    *
# With the largest size 9 tree looking like this:
#
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
#          *

# function to print a single christmas tree
def make_tree(base):
    # use the largest limbs of the tree, those at the bottom, to calculate
    # how many lines will be necessary to make the tree, plus 1 for the
    # stump of the tree and iterate through from the smallest branch size
    # for the top of the tree, until reach the final limb size
    for limb in range(1,base+1):
        # wrap a print statment around
        # total final size minus the iterable worth of spaces
        # the the iteratable number of astrixes
        # the iterable minus 1 number of spaces
        # and again the  total final size minus the iterable number of spaces
        # onto one line
        print((base-limb)*' ',''.join((limb*'*',(limb-1)*'*')),(base-limb)*' ')
    # then print the final size minus one spaces twice, with an asgtrix
    # in the center for the tree stump
    print((base-1)*' ','*',(base-1)*' ')
    # print a new line for space between the next tree
    print()

# the sizes of the trees to print, as a list to iterate through
sizes = (3,4,5,6,7,8,9)

# make a list of the tree sizes, mapped to the functuion to make the tree
# with a [-1] so that the last item of the list doesn't print none to the
# output
list(map(make_tree,sizes))[-1]
