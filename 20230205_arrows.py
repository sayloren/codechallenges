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

# dictionary with the arrows, tried using the unicode values, but they
# wanted the actual arrows
arrow_dict = {'↙':[-1,-1],'↲':[-1,-1],'⇙':[-1,-1],
              '←':[-1,0],'⇐':[-1,0],'⇦':[-1,0],
              '↖':[-1,1],'↰':[-1,1],'⇖':[-1,1],
              '↓':[0,-1],'⇓':[0,-1],'⇩':[0,-1],
              '↔':[0,0],'↕':[0,0],'⇔':[0,0],'⇕':[ 0,0],'⥀':[ 0,0],'⥁':[ 0,0],
              '↑':[0,1],'⇑':[0,1],'⇧':[0,1],
              '↘':[1,-1],'↳':[1,-1],'⇘':[1,-1],
              '→':[1,0],'⇒':[1,0],'⇨':[1,0],
              '↗':[1,1],'↱':[1,1],'⇗':[1,1]}

# the starting coords are 0,0
initial_coords = [0,0]

# from sys the args are passed in as a list of arrows
# go through one at a time because they want to print each as a step
for arg in sys.argv[1:]:
    # zip the inital and the step together and use map to sum them
    # make into list afterwards other wise the page just prints a map object
    new_coord = list(map(sum,zip(initial_coords,arrow_dict[arg])))
    # print it in the weird format they want
    print('{0} {1}'.format(new_coord[0],new_coord[1]))
    # update the intial to be the new coord for next step
    initial_coords = new_coord
