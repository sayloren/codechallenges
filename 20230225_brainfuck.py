# code golf challenge
# https://code.golf/brainfuck#python
# wren 20230225

# Brainfuck is a minimalistic esoteric programming language created by Urban Müller in 1993.

# Assuming an infinitely large array, the entire brainfuck alphabet matches the following pseudocode:
# >	ptr++
# <	ptr--
# +	array[ptr]++
# -	array[ptr]--
# .	print(chr(array[ptr]))
# [	while(array[ptr]){
# ]	}

# ptr++ means increment the pointer one step to the right - next cell
# ptr-- means decrement the pointer one step to the left - back cell
# array[ptr]++ means increment the byte at the pointer
# array[ptr]-- means decrement the byte at teh pointer
# print(chr(array[ptr])) means output the byte at the pointer
# while(array[ptr]){ means 

# Write a program that will receive various brainfuck programs as arguments and execute each program in turn. 

program_dict = {'>':'ptr++','<':'ptr--','+':'array[ptr]++','-':'array[ptr]--','.':'print(chr(array[ptr]))','[':'while(array[ptr]){',']':'}'}


import sys

# Printing
print('Hello, World!')

# Looping
for i in range(10):
    print(i)

# Accessing arguments
for arg in sys.argv[1:]:
    print(arg)



