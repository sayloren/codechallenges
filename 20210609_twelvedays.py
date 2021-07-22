# code golf challenge
# https://code.golf/12-days-of-christmas#python
# wren 20210609

# Print the lyrics to the song The 12 Days of Christmas:

# Notes:
# not particullary happy with my solution - the initalized list seems too
# wordy to me

# the initalled list of strings of days, im going to use these terms
# to iterate throguh and .fromat in, so that i dont have to type out the
# full thing every time, and just reference when i need it
days = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth',
'Ninth','Tenth','Eleventh','Twelfth']

# the initalized list of strings for each occurance at that day, same
# concepts as the days - could perhaps zip them together?
num_days = ['A Partridge in a Pear Tree.','Two Turtle Doves, and',
'Three French Hens,','Four Calling Birds,','Five Gold Rings,',
'Six Geese-a-Laying,','Seven Swans-a-Swimming,','Eight Maids-a-Milking,',
'Nine Ladies Dancing,','Ten Lords-a-Leaping,','Eleven Pipers Piping,',
'Twelve Drummers Drumming,']

# for the length of the initalled days in the lsit (twelve days), begining with
# 0 as range is zero based, and there is no reason to start with
# 1 as im not working with digits
for day in range(0,len(days)):
    # first print the first line of the stanza, which is contains the infered
    # day of christmas, using a \n in the middle to make a new line for
    # each section of the song
    print('On the {0} day of Christmas\nMy true love sent to me'.format(days[day]))
    # print the stanzas of the full gifts per day, backwards to the current day
    # with a \n to make a new line between each line, from the reversed list
    # of lines per day, using the * to unpack the list to print statements
    print(*num_days[day::-1], sep='\n')
    # after the whole stanza, print an empty line, before going back through
    # the for loop for the next day
    print()
