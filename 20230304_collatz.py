# code golf challenge
# https://code.golf/collatz#python
# wren 20230304

# The Collatz conjecture states that, for any positive integer n, 
# it will eventually reach 1 by repeatedly applying the following procedure:

#     If n is even, divide it by 2.
#     If n is odd, multiply by 3 and then add 1.

# The number of steps needed for n to reach 1 is called its stopping time. 
# For example, the stopping time of 10 is six:

# 10 → 5 → 16 → 8 → 4 → 2 → 1

# Print the stopping times of all the numbers from 1 to 1,000 inclusive, each on their own line. 

# collatz function takes in an int
def collatz(i):
    # if divisible by 2 returns the int divided by 2
    if i % 2 == 0:
        return(int(i/2))
    # if odd, returns the int times 3 plus 1
    else:
        return(int((i*3)+1))
    
# loop through 1000 inclusive
for i in range(1,1001):
    # initate count for how many times the int has to pass through the collatz function
    count = 0
    # while the int is greater than 1 (or just not equal to 1)
    while i > 1:
        # run through the collatz function, with the returned value the new int going into the while
        i = collatz(i)
        # add to the count for how mamy times its passed through the collatz
        count += 1
    # print the final count
    print(count)