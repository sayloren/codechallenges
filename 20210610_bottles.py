# code golf challenge
# https://code.golf/99-bottles-of-beer#python
# wren 20210610

# Print the lyrics to the song 99 Bottles of Beer:

# note:
# not super happy with my solution - feels like too much string text

# for the requred 99 bottles, starting from 99 and ending at 2
# because the language is slightly different for the last 1 and 0
# lines - there is probalby a better way - like using [:-1] or something for
# excluding the s from bottles ect
for bottle in range(99,2,-1):
    # print the line with .format() to print the correct values
    # in the stanza, with \n to make new line splits
    print('{0} bottles of beer on the wall, '
    '{0} bottles of beer.\nTake one down and '
    'pass it around, {1} bottles of beer on the wall.'.format(bottle,bottle-1))
    # make a new line print between the next stanza
    print()

# after through to 2, print the final section as a string, because the language
# plural form of some of the words is different as well as the ending
print('2 bottles of beer on the wall, '
'2 bottles of beer.\nTake one down and '
'pass it around, 1 bottle of beer on the wall.\n\n'
'1 bottle of beer on the wall, 1 bottle of beer.\n'
'Take one down and pass it around, no more bottles of beer on the wall.\n\n'
'No more bottles of beer on the wall, no more bottles of beer.\n'
'Go to the store and buy some more, 99 bottles of beer on the wall.'
)
