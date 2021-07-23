# code golf challenge
# https://code.golf/emojify#python
# wren 20210720

# Given each of the following ASCII emoticons print the corresponding Unicode emoji.

# Note despite how they appear below, there are no spaces in the emoticons.
# there is an emoji module that code golf doenst support
# import emoji
# and i could use just a dictionary, but python cant read the emojis as they are
# emoticon_dictionary = {':-D':😀,':-)':🙂,':-|':😐,':-(':🙁,':-\\':😕,
# ':-*':😗,':-O':😮,':-#':🤐,'\':-D':😅,'\':-(':😓,':\'-)':😂,':\'-(':😢,
# ':-P':😛,';-P':😜,'X-P':😝,'X-)':😆,'O:-)':😇,';-)':😉,':-$':😳,':-':😶,
# 'B-)':😎,':-J':😏,'}:-)':😈,'}:-(':👿,':-@':😡}

# emoticon_dictionary = {':-D':'U+1F600',':-)':'U+1F642',':-|':'U+1F610',
# ':-(':'U+1F641',':-\\':'U+1F615',':-*':'U+1F617',':-O':'U+1F62E',
# ':-#':'U+1F910','\':-D':'U+1F605','\':-(':'U+1F613',':\'-)':'U+1F602',
# ':\'-(':'U+1F622',':-P':'U+1F61B',';-P':'U+1F61C','X-P':'U+1F61D',
# 'X-)':'U+1F606','O:-)':'U+1F607',';-)':'U+1F609',':-$':'U+1F633',
# ':-':'U+1F636','B-)':'U+1F60E',':-J':'U+1F60F','}:-)':'U+1F608',
# '}:-(':'U+1F47F',':-@':'U+1F621'}

import sys

# the dictionray with the symbol strings for the emojis as the keys
# and the unicode as the values from the below website
# http://www.unicode.org/emoji/charts/full-emoji-list.html
emoticon_dictionary = {':-D':'\U0001F600',':-)':'\U0001F642',':-|':'\U0001F610',
':-(':'\U0001F641',':-\\':'\U0001F615',':-*':'\U0001F617',':-O':'\U0001F62E',
':-#':'\U0001F910','\':-D':'\U0001F605','\':-(':'\U0001F613',':\'-)':'\U0001F602',
':\'-(':'\U0001F622',':-P':'\U0001F61B',';-P':'\U0001F61C','X-P':'\U0001F61D',
'X-)':'\U0001F606','O:-)':'\U0001F607',';-)':'\U0001F609',':-$':'\U0001F633',
':-':'\U0001F636','B-)':'\U0001F60E',':-J':'\U0001F60F','}:-)':'\U0001F608',
'}:-(':'\U0001F47F',':-@':'\U0001F621'}

# seting the inputs from the website as varialbe, using standard inputs
# the [1:] is beacue the arguments are given in a list, and this takes
# everything except the first item, which should be 'python' or something
symbols = sys.argv[1:]

# as a list comprehension, print the values for each key in the list of symbols
# ecluding the last, which is a list of none
[print(emoticon_dictionary[emoji]) for emoji in symbols][-1]

# could also write the last line as the below, which i think might be faster
# which is print the list with join with new lines between each item in the list
# the list is a list comprehension getting the values for each key in the
# variable symbols
print('\n'.join([str(emoticon_dictionary[emoji]) for emoji in symbols]))
