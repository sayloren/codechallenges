# code golf challenge
# https://code.golf/divisors#python
# wren 20210710

# A number is a divisor of another number if it can
# divide into it with no remainder.

# Print the positive divisors of each number from
# 1 to 100 inclusive, on their own line, with each
# divisor separated by a space.

# first method
# make a list of the range of teh requested dimenstions, plus one for zero based
my_range = list(range(1,100+1))
# for each value in the final number inclusive range
for intager in my_range:
    # initalize a list to collect the list of divisors for the intager
    # being iterated over
    collect = []
    # make a list with the range from one to the iterable intager plus 1 for
    # zero based, to loop over in the next for loop
    # i feel like this could be done by extracting the previous range
    # maybe something like for intager, div in zip(my_range, some corresponding
    # list containing the range of values up until the iterable from the original
    # list) like: list(range(my_range[i])
    num_range = list(range(1,intager+1))
    # for each value in the range, from one to the first iterable
    for num in num_range:
        # if that second iterable divies perfectly into the first iterable,
        # collect the second iterable as a string on to the end of the list
        # collection
        if intager%num == 0:
            collect.append(str(num))
    # now print each itme in the list collectino with spaces between them
    # using join
    print(' '.join(collect))

# second method
# functin for printint the divisors, taking in the value to check append
# printing out the divisors to one line seperaed by spaces
def print_divs(large):
    # initalize a list to collect the divisors
    collect=[]
    # for each value in a range of 1 to the input value plus 1
    for intager in range(1,large+1):
        # if the input value is perfectly divisible, collect the string
        # of that value into the collection
        if large%intager==0:
            collect.append(str(intager))
    # then print the final collection seperated by spaces with join
    print(' '.join(collect))

# the list containing the requested numbers as a range begining from 1 to 100
my_range = list(range(1,100+1))
# make a list of the list of values mapped to the function, minus the last
# element in the list which prints none
list(map(print_divs,my_range))[-1]

# third method
# functin for printint the divisors, taking in the value to check append
# printing out the divisors to one line seperaed by spaces
def print_divs(input):
    # initalize a list to collect the divisors
    collect=[]
    # make a list with the range from 1 to the input value plus 1 for zero based
    num_range=list(range(1,input+1))
    # with list comprehention, append to the collection list a string of those
    # values in the range 1 to the input value that perfectly divide without
    # any remainders
    [collect.append(str(divisor)) for divisor in num_range if input%divisor==0]
    # now print that final list collection into a new line seperated by spaces
    # with join
    print(' '.join(collect))

# the list containing the requested numbers as a range begining from 1 to 100
my_range = list(range(1,100+1))
# make a list of the list of values mapped to the function, minus the last
# element in the list which prints none
list(map(print_divs,my_range))[-1]
