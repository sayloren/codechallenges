# code golf challenge
# https://code.golf/catalan-numbers#python
# wren 20230226

# The nth Catalan number can be expressed as C(n) = binomial(2n,n)/(n+1).
# Print the first 100 Catalan numbers, from C(0) to C(99) inclusive, each on their own line.
# Note: C(99) is 57 digits long, and is greater than 2187

# catalan number is the number of ways you can triangulate a polygon
# https://www.youtube.com/watch?v=LwqxXLwoenE
# cn = c0*cn-1 + c1*cn-2 + c2*cn-3 ... cn*c0
# https://www.youtube.com/watch?v=n6uYe_DmYe8
# c0 - 1, cn+1 = cicn-i

# there must be a recurisve way to do this....

collect_catalan = [1]

def catalan(n):
    # make a range and a reverse range expansion from 0 to n for the catalan subscripts
    # use the ranges as indexes to access the respecitve values in the catalan list values
    # zip the two together and multiply each of the pairs
    # sum the results
    return sum([i1 * i2 for i1, i2 in zip([collect_catalan[i] for i in range(0,n)],[collect_catalan[i] for i in range(n-1,-1,-1)])])

# for the requested range, insert each addition at the correct index in the catalan list
for n in range(1,100):
    collect_catalan.insert(n,catalan(n))

# print each value in catalan list to new line
print(*collect_catalan,sep='\n')





