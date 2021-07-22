# code golf challenge
# https://code.golf/fizz-buzz#python
# wren 20210607

# Print the numbers from 1 to 100 inclusive, each on their own line.
# If, however, the number is a multiple of three then print Fizz instead,
# and if the number is a multiple of five then print Buzz.
# For numbers which are multiples of both three and five then print FizzBuzz.

# iterate through reange of required numbers - plus one because range is
# zero based if 3 print fizz, if 5 print buzz, and if both fizzbuzz
# i feel like there should be a way to have the 15/fizzbuzz not be a
# seperate condition
for number in range(1,101):
    # if there are no remainders for the number in the range divied by 15
    # condition for both 5 and 3 - 15 is lowest divisor, where both fizz and buzz
    if number%15==0):print('FizzBuzz')
    # if there are no remainders for the number in the range divied by 3
    # elif condition for just 3 - fizz
    elif number%3 ==0:print('Fizz')
    # if there are no remainders for the number in the range divied by 5
    # elif condition for just 5, buzz
    elif number%5==0:print('Buzz')
    # else none of the conditions, just print the number
    else:print(number)

# alternative approach in one liner
# for loop the same, but conditions where there are no remainders for the
# divisability are all wrapped in a print statement
for number in range(1, 101): print("Fizz"*(number%3==0)+"Buzz"*(number%5==0) or str(number))
