# code golf challenge
# https://code.golf/arabic-to-roman#python
# wren 20210613

# For each arabic numeral argument print the same number in roman numerals.
# didnt end up needing this, as did an interatble update
    # 50:'L',100:'C',500:'D',1000:'M'}
# import sys
# sys.argv[1:]

# need to import sys in order to take in the arguments given by the website
import sys

# get the inputs passed in, from the second, as the first couple of
# args in will be depolytin the language, script or whatever
# name as variable to iterate through
arubic_numbers = sys.argv[1:]

# the dictionary with the intagers to numeral conversions to use to look up
# and convert
roman_numeral = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',
                    8:'VIII',9:'IX',10:'X',0:'N'}

# for the arabic numbers given by the website, iterate through the list
for arabic in arubic_numbers:
    # first initalize a conversion list to add into
    roman_conversion = []
    # in a list comprehension, seperate out each digit as a string, to make a
    # list of strings of each digit in the arabic number given
    arabic_string = [intager for intager in str(arabic)]
    # for each of the digit values in the list of strings from the arabic number
    # first convert the value back to an intager, then use the dictionary
    # to look up what the roman numeral conversion is, and append to the
    # initalzed list of converted values
    for intager in arabic_string:
        roman_conversion.append(roman_numeral[int(intager)])
    # reverse the order of the list of converted digits, because the
    # updating the symbol by position is conditional on the legnth
    # of the number of positions, so the list order has to start from
    # one and end at the largest position value (or could have the
    # condition be a [-1] type selector)
    reverse_final = roman_conversion[::-1]
    # conditally update the symbols for the values by which position
    # the number is in the list of digit value strings
    # update in place
    if len(reverse_final) > 1:
        reverse_final[1]=reverse_final[1].replace('X','C').replace('I','X').replace('V','L')
    if len(roman_conversion) > 2:
        reverse_final[2]=reverse_final[2].replace('X','M').replace('I','C').replace('V','D')
    if len(reverse_final) > 3:
        reverse_final[3]=reverse_final[3].replace('I','M')
    # filter out the 'N' in the list of strings, which is a place holder for
    # there is nothing in that position ie 105 - so N would be at the 10's
    # position, to avoid accidentally intepreting the 105 as 15 when
    # converted with the dictionary
    drop_zero =list(filter(('N').__ne__, reverse_final))
    # now print the list of string roman numberals from the last item in the
    # list to the first so that the final printed value is ordered correctly
    # using .join to print the items in the list of strings together with
    # no spaces between
    print(''.join(str(numeral) for numeral in drop_zero[::-1]))

# reverse, pop, convert, add to final list, recursion

# another method:
# function to run the conversion, taking in the arabic number
# and printing out the final converted roman numeral
def convert(arabic):
    # first initalize a conversion list to add into
    roman_conversion = []
    # in a list comprehension, seperate out each digit as a string, to make a
    # list of strings of each digit in the arabic number given
    arabic_string = [intager for intager in str(arabic)]
    # for each of the digit values in the list of strings from the arabic number
    # first convert the value back to an intager, then use the dictionary
    # to look up what the roman numeral conversion is, and append to the
    # initalzed list of converted values
    for intager in arabic_string:
        roman_conversion.append(roman_numeral[int(intager)])
    # make a new final list with everything from the conversion except for the
    # ones position, which is already correctly rendered
    final_roman_conversion = [roman_conversion[-1]]
    # pop off that last ones position from the old list
    roman_conversion.pop()
    # while there is still something in the old list, perform the following
    # replacemtnes
    while len(roman_conversion) > 0:
        # on the last item in the list, which will go through
        # tens, then hundreds, then thousand positions with each pass
        # through the while loop, replace for teh appropriate
        # symbols - first replace any x with ls, then if there are
        # i replace it with x, and last if there are v replace it
        # with l, so that each successive replace only occurs on
        # where necessary
        roman_conversion[-1].replace('X','L').replace('I','X').replace('V','L')
        # add that converted last list item from the old
        # list to the final new list and remove it from the old list that is
        # being looped over in the while loop
        final_roman_conversion.append(roman_conversion.pop())
    # from the final conversion list, remove any n, which is place holding
    # zeros in which ever position, so that that position will not
    # be accidentally dropped
    final_roman_conversion.remove('N')
    # print the list of intagers converted to strings from last to first
    # so the roman numeral is in the correct order, without any
    # spaces between each symbol
    print(''.join(str(digit) for digit in final_roman_conversion[::-1]))



# def convert(arabic):
#     roman_conversion = []
#     arabic_string = [intager for intager in str(arabic)]
#     for intager in arabic_string:
#         roman_conversion.append(roman_numeral[int(intager)])
#     reverse_final = roman_conversion[::-1]
#     if len(reverse_final)==1:
#         pass
#     elif len(reverse_final)==2:
#         reverse_final[1]=reverse_final[1].replace('X','L').replace('I','X').replace('V','L')
#     elif len(reverse_final)==3:
#         reverse_final[1]=reverse_final[1].replace('X','L').replace('I','X').replace('V','L')
#         reverse_final[2]=reverse_final[2].replace('X','M').replace('I','C').replace('V','D')
#     else:
#         reverse_final[1]=reverse_final[1].replace('X','L').replace('I','X').replace('V','L')
#         reverse_final[2]=reverse_final[2].replace('X','M').replace('I','C').replace('V','D')
#         reverse_final[3]=reverse_final[3].replace('I','M')
#     print(''.join(str(i) for i in reverse_final[::-1]))
