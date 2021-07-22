# code golf challenge
# https://code.golf/fibonacci#python
# wren 20210606

# Print the first 31 Fibonacci numbers from F0 = 0 to F30 = 832040
#(inclusive), each on a separate line.

# initiate list of Sequence
# start with the first two values in the series, 0 and 1 in a list
sequence = [0,1]

# while there are less than 31 values in the sequence, loop
# 31 is the requested length
while len(sequence) < 31:
    # append to the intialized list the sum of the last two numbers in the list
    sequence.append(sum(sequence[-2:]))

# just to make everythin print on its own line, iterate through list of
# sequence
for number in sequence:
    print(number)


# alternative approach
# initiate list of Sequence
# start with the first two values in the series, 0 and 1
sequence = [0,1]

# print each of the inital sequence to its own line,
# as requested, starting from the initalized list
print(0)
print(1)

# while less than the required series length of 31, continue
while len(sequence) < 31:
    # append to the sequence list the sum of the last two values in the list
    sequence.append(sum(sequence[-2:]))
    # print the sum of the last two values, now the lists last item to its own line
    print(sequence[-1])
