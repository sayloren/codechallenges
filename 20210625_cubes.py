# code golf challenge
# https://code.golf/cubes#python
# wren 20210625

# Draw 7 cubes in increasing size using "╱" (U+2571) for
# the diagonal edges, "│" (U+2502) for the vertical edges,
# "─" (U+2500) for the horizontal edges, and "█" (U+2588)
# for the vertices. The cubes should range from size 1 to
# size 7 with a blank line between each cube. A size 1 cube
# should look like:
#
#   █────█ # 2,4
#  ╱    ╱│ # 1,1
# █────█ │
# │    │ █
# │    │╱
# █────█
# 4,1,2
# And a size 7 cube should look like:
#
#         █────────────────────────────█ # 8,28
#        ╱                            ╱│
#       ╱                            ╱ │
#      ╱                            ╱  │
#     ╱                            ╱   │
#    ╱                            ╱    │
#   ╱                            ╱     │
#  ╱                            ╱      │
# █────────────────────────────█       │
# │                            │       │
# │                            │       │
# │                            │       │
# │                            │       │
# │                            │       │
# │                            │       │
# │                            │       █
# │                            │      ╱
# │                            │     ╱
# │                            │    ╱
# │                            │   ╱
# │                            │  ╱
# │                            │ ╱
# │                            │╱
# █────────────────────────────█
# 28,7,14

# function to print each cube
def make_cube(size):
    # make a variable with the first edge of the top of the cube as a
    # string containing, joined with no spaces, corner characters
    # between which is the total size of the cube times 4
    width_edge = ''.join((corner,width*(size*4),corner))
    # print the above varaialbe, for the first line of the cube,
    # joining without spaces, the total size number of spaces plus 1 for
    # style followed by the variable
    print(''.join((' '*(size+1),width_edge)))
    # make variables for differnt aspects of the top planes of the cube as
    # strings of values, the number of spaces in the plane is the size
    # of the cube times 4 then the width of the plane is those spaces
    # joined between the special character for the edges of the top plane
    plane_space = ' '*(size*4)
    width_plane = ''.join((length,plane_space,length))
    # the dimensions of the cube, to make the top plane plus the begingin
    # of the side visible from an angle, zip together ranges from
    # zero (says -1 as zero based) to the size minus 1 for the side of the
    # cube, and range beging with the size, counting down to zero for the
    # empty space until the top plane is printed, giving the perception of
    # depth in the printed image
    for space,side in zip(range(-1,size-1),range(size,0,-1)):
        # with these two paired values, print the joined strings with the
        # increaseing spaces moving down the printed lines next to width of
        # the top plane, then the increasing number of spaces for the side of
        # the cube, followd by the special character for height used for the
        # boundary side of the cube
        # extra: it would be interesting to do this as a split of the size
        # between the two diagonal planes
        print(''.join((' '*side,width_plane,' '*(space+1),height)))
    # print the joined strings for the width edge again, used again from the
    # first printed line, followed by the number of spaces as the size of the
    # cube, then the special character used for height
    print(''.join(((width_edge),' '*(size),height)))
    # variable containing the string for the front plane of the cube, joining
    # strings for the plane space, surrounded by the special height characters
    height_plane = ''.join((height,plane_space,height))
    # for one to the size of the cube, print a joined string of the plane
    # made for the height of the cube, followed by the same number of spaces
    # as the size of the cube, and the special height character to make the
    # front of the and the side of the cube section
    for flat in range(1,size):
        print((''.join((height_plane,' '*(size),height))))
    # print a joined string with the plane made for the heigh, followed by
    # the same number of spaces as the cube size and the special corner character
    # make the bottom half of the front of the cube, next to the diminishing
    # side of the cube
    print((''.join((height_plane,' '*(size),corner))))
    # for the size of the cube minus one, to 0 (as -1 for 0 based range),
    # print the joined string of the height plane string follwed by the
    # decreasing plane of the cube side so that the side of teh cube joins the
    # front plane, followed by the legth character
    for side in range(size-1,-1,-1):
        print((''.join((height_plane,' '*side,length))))
    # print the width edge one last time, followed by an empty print to make
    # a new line between the next cube to be printed
    print(width_edge)
    print()

# initalize the special characters in their own variables for
# more descriptive reference
corner = '█'
length = '╱'
height = '│'
width = '─'
# a list of the requested sizes, given as a range as they are increaseing
# from 1 to 8
sizes = list(range(1,8))
# a list maping the list of sizes to the function printing the cube, minus
# the last item in this list which is None for reasons i dont understand
list(map(make_cube,sizes))[-1]
