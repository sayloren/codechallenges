# code golf challenge
# https://code.golf/happy-numbers#python
# wren 20210608

# A happy number is defined by the following Sequence:
# Starting with any positive integer, replace the number
# by the sum of the squares of its digits in base-ten,
# and repeat the process until the number either equals 1
# (where it will stay), or it loops endlessly in a cycle
# that does not include 1. Those numbers for which this
# process ends in 1 are happy numbers, while those that do
# not end in 1 are sad numbers.
# For example, 19 is happy, as the associated Sequence is:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1.
# Print all the happy numbers from 1 to 200 inclusive, each on their own line.

# notes
# kind of cheated by just printing 1, though 1 should be accepted by the func

# function happy
def happy(number):
    # the sum of each digit in the input number raised to the second power
    # the number is converted to a string in order to iterate through the
    # digits, then each digit is converted back to an intager and squared
    # each squared digit is then added together
    sum_number = sum(int(digit)**2 for digit in str(number))
    # if that final sum of squared digits is already within the list (after the
    # first list value) of sums, initialized in the for loop handing the
    # number to the function, the function passes, being in this list means
    # that we have already tried out the squared digits of the number and
    # that this is not a happy number
    if sum_number in contain[1:]:
        pass
    # elif conditionally, the sum of the squared digits is 1, this means
    # that we have fund a happy number, and we can now print the First
    # value in the initallized list, which is the number we are iterating
    # through
    elif sum_number == 1:
        print(contain[0])
    # if neither of these conditions are met, it measn that we have not yet
    # reached our decision point for whether this is a happy number, and
    # must recursivally pass the sum of the square digits to the happy function
    # after first adding the sum to the initallized list for checking in the
    # next pass
    else:
        contain.append(sum_number)
        happy(sum_number)

# for the requested range plus one for range is zero based
for number in range(1,200+1):
    # initialize the number iterating through as the first value in a list
    # so that the function can work upon the variable
    contain = [number]
    # input the number iterating through to the happy function
    happy(number)
