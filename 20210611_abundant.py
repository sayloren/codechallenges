# code golf challenge
# https://code.golf/abundant-numbers#python
# wren 20210611

# An abundant number is a number for which the sum of its
# proper divisors (divisors not including the number itself)
# is greater than the number itself. For example 12 is abundant
# because its proper divisors are 1, 2, 3, 4, and 6 which add up to 16.

# Print all the abundant numbers from 1 to 200 inclusive, each on their own line.


# function, check, which checks if a number in the requested range is abundant
# requires no arguments, just run as is

def check ():
    # for the requested range 1 to 200 +1 because range is zero based
    for candidate in range(1,1000+1):

        # intialize the variable sum at 0 in order to add to it later
        # and conditionally check the value, this is the value of
        # the sum of the divisors of the iterating number
        sum = 0

        # for j in the range of half the iterable - as half way is divisible
        # by 2, so going beyond would be redundant and uncessary computations
        for denominator in range(1,int(candidate/2)+1):

            # if the original value is perfectly divisable by the
            # subset range up to half the origanl value, add that
            # subset range value to the perveiously set sum variable
            # basically adding together the divisors
            if candidate%denominator==0:
                sum+=denominator

        # afer checking for all the divisors, and adding them together,
        # check if the sum is greater than the original iterating value
        # if it is, print the value, as it is an abundant number
        if sum > candidate:
            print(candidate)

        # if this condition is not met, it is not an abundant number
        # and passes on to the next number in the range
        else:
            pass

check()