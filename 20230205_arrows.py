# code golf challenge
# https://code.golf/arrows#python
# wren 20230205

# Starting at [0, 0] print the cumulative 
# result of applying each of the given Unicode 
# arrow arguments. The arrows will be a 
# random combination of these:

# [-1, -1]	↙ U+2199, ↲ U+21B2, ⇙ U+21D9
# [-1,  0]	← U+2190, ⇐ U+21D0, ⇦ U+21E6
# [-1,  1]	↖ U+2196, ↰ U+21B0, ⇖ U+21D6
# [ 0, -1]	↓ U+2193, ⇓ U+21D3, ⇩ U+21E9
# [ 0,  0]	↔ U+2194, ↕ U+2195, ⇔ U+21D4, ⇕ U+21D5, ⥀ U+2940, ⥁ U+2941
# [ 0,  1]	↑ U+2191, ⇑ U+21D1, ⇧ U+21E7
# [ 1, -1]	↘ U+2198, ↳ U+21B3, ⇘ U+21D8
# [ 1,  0]	→ U+2192, ⇒ U+21D2, ⇨ U+21E8
# [ 1,  1]	↗ U+2197, ↱ U+21B1, ⇗ U+21D7


import sys

# dictionary with the arrows
arrow_dict = {('U+2199','U+21B2','U+21D9'):[-1,-1],
              ('U+2190','U+21D0','U+21E6'):[-1,0],
              ('U+2196','U+21B0','U+21D6'):[-1,1],
              ('U+2193','U+21D3','U+21E9'):[ 0,-1],
              ('U+2194','U+2195','U+21D4','U+21D5','U+2940','U+2941'):[ 0,  0],
              ('U+2191','U+21D1','U+21E7'):[ 0,1],
              ('U+2198','U+21B3','U+21D8'):[ 1,-1],
              ('U+2192','U+21D2','U+21E8'):[ 1,0],
              ('U+2197','U+21B1','U+21D7'):[ 1,1]}

# the starting coords are 0,0
initial_coords = [0,0]


# return the coords for an input arrow
def return_coord(input_arrow):
    # first finds the tuple that the arrow is
    # a key in, then returns the corresponding coord
    for key in arrow_dict.keys():
        if input_arrow in key:
            return arrow_dict.get(key)

for arg in sys.argv[1:]:
    arrow_coord = return_coord(arg)
    new_coord = map(sum,zip(initial_coords,arrow_coord))
    print(new_coord)
    initial_coords = new_coords





any(key in sub for sub in arrow_dict)

print(arrow_dict.get(value))


import sys

# Printing
print('Hello, World!')

# Looping
for i in range(10):
    print(i)

# Accessing arguments
for arg in sys.argv[1:]:
    print(arg)




