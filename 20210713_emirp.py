# code golf challenge
# https://code.golf/emirp-numbers#python
# wren 20210713

# An emirp (prime spelled backwards) is a prime
# number that results in a different prime when
# its decimal digits are reversed. For example both 13 and 31 are emirps.

# Print all the emirp numbers from 1 to 1000
# inclusive, each on their own line.

# notes:
# aparently list comprehensions are really slow
# add docstring
# tim says comments should be what why and how

def remainders(number):
    # get the remainder of the number by the range of each number up to half
    # the number because unecessary to compute second half (divisble by 2)
    # with list comprehension
    left_over = [number%demoninator for demoninator in range(1,int(number/2)+1)]

    # count the number of zeros in the remainders list as 0s indicate
    # how many numbers the number is perfecly divisible by - only one
    # 0 would make it prime, as it would only be divisible by 1
    count_zero = left_over.count(0)

    # return 0 for prime and 1 for not prime to make sorting easier
    # with conditional
    return(0 if (count_zero ==1 or count_zero==0) else 1)

# 1 to one thousand range to work through with plus one as range is zero based
# into a list
full_range = list(range(1,1000+1))

# reverse the digits of the range in the same order as the original ranges
# list using list comprehension where each value is converted to a docstring
# reversed, then converted back to an integer
reverse_range=[int(str(number)[::-1]) for number in full_range]

# check prime for each value in both ranges created into new lists mapping
# both range and reversed range to the remainders function where a list
# of 0 and 1 are returned where 0 is a prime and 1 is not
sum_remainder = list(map(remainders,full_range))
sum_remainder_reverse = list(map(remainders,reverse_range))

# zip the two lists for the ranges and get the sums with list comprehension
# where each matched pair in zipped lists are added together into a new
# single list
zip_remainder = [number+reversed for number,reversed in zip(sum_remainder,sum_remainder_reverse)]

# get the full range values where both forward and back int are prime
# by looking at where in zip remainder positions are 0, which indicates
# that there is nothting besides 1 which perfectly divides the number
# with list comprehension, making an index for selecting from list
# using the range of the total length of the zip remaind4rs list
prime_location = [summed for summed in range(len(zip_remainder)) if zip_remainder[summed] == 0]

# use the locations of those prime numbers in prime_location to
# select out the original numbers in the first variable, full ranges
# from 1 to 1000, using a list comprehension indexing
prime_values = [full_range[primes] for primes in prime_location]

# filter palendromic values because for whatever reason they are not considered
# emirps even though they technically are, using a list comprehnsion with
# a conditional where the value iterated over, is not equal to the same value,
# converted to a string, reveresd, and then converted back to an intager
filer_palendromes = [emirp for emirp in prime_values if emirp!=int(str(emirp)[::-1])]

# print each emirp number to new line, excluding the last 'None' value that
# prints, for some reason i dont understand
[print(i) for i in filer_palendromes][-1]
