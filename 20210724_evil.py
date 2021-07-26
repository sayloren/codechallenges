# code golf challenge
# https://code.golf/evil-numbers#python
# wren 20210724

# An evil number is a non-negative number that has an
# even number of 1s in its binary expansion.
#
# Print all the evil numbers from 0 to 50 inclusive, each on their own line.
#
# Numbers that are not evil are called odious numbers.

# note: im not totally happy with my solution - there is a conditional under
# a for loop and it feels sad. i tried to use map and yeild, but couldnt
# figure it out

# https://www.instructables.com/How-to-Convert-Numbers-to-Binary/
# radix
# 318
# 300 + 10 + 8
# 3x10^2 + 1x10^1 + 8x10^0
# converting from binary
# 1010
# 1000 + 000 + 10 + 0
# 1x2^3 + 0x2^2 + 1x2^1 + 0x0^0
# 2^3+2^1 = 10
# decimal to Binary
# 122/2 = 61 remainder 0
# 61/2 = 30 remainder 1
# 30/2 = 15 remainder 0
# 15/2 = 7 remainder 1
# 7/2 = 3 remainder 1
# 3/2 = 1 remainder 1
# 1/2 = 0 remainder 1
# 1111010 (note: reversal of the order for the yeilded remainders)

# perform the sequence of divisions by 2 that occurs during converting to
# binary but only passing along the number of times the binary is a 1
# instead of a 0 instead of actually making the number
def binarize(number):
    # make count a global variable so that we can add to it from inside this
    # function (im a bit frusterated with this part, i tried a lot of different
    # approaches, and this is the only one that worked, but im unsatisfied)
    global count
    # if the number is more than 0 condition - other wise there are no more
    # division by 2 to perform
    if number > 0:
        # add to the current count variable the remainder of the division by 2
        # this is the binary value at that position in the final binary number
        # but i only want to count the 1's, so im not doing anything else
        count+=(number%2)
        # recursivly call the function on the number, with // it rounds the
        # division down to and to an int
        binarize(number//2)

# https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
# https://math.stackexchange.com/questions/2888548/what-is-a-binary-expansion-of-a-real-number
# make the range requested to binarize, plus 1 to be inclusive of 50
my_range = list(range(0,50+1))

# for each value in my requested range
for number in my_range:
    # initalize the counter
    count = 0
    # run the function for the number
    binarize(number)
    # if the number of 1's in the final binary number is an even number,
    # so it divides perfectly by 2 with no remainders, it is an evil number
    # and so the number is preinted to standardoutput
    if count%2==0:
        print(number)

# this is a stand alone function from the problem, it makes the binary number
# for an intager
def binarize(number):
    # check if the number is 0, because there will be no need to continue
    # to reduce from there - stopping condition is implicit
    if number > 0:
        # get if the number is evenly divided by two and append the remainde
        # into the initalized list to capture the final binary value
        # dont acually need to know what the binary is, but going to for the sake
        # of learning
        remainder = number%2
        binary.append(remainder)
        # divide the number by 2, rounding always rounds down, so no need to
        # use something like math.floor, going to do // which has the same effect
        # of roudning or wrapping in int()
        result = number//2
        # recursively loop through the function with the result of the
        # number divided by 2
        binarize(result)

# whatever number to convert
num = 19
# initalize the list to capture remainders making up the binary
binary = []
# run the function to convert the number
binarize(num)
# reverse the list with the remainders so that the binary number is oriented
# correctly
binary.reverse()

# benchmark speed of binarizing function

# using time
import time

# 0.0018352179999965301
def binarize_if(number):
    if number > 0:
        binary.append(number%2)
        binarize_if(number//2)

start_time = time.perf_counter()
number = 19
binary = []
binarize_if(number)
count = binary.count(1)
end_time = time.perf_counter()
length = end_time - start_time
print(binary,count,length)
