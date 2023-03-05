# code golf challenge
# https://code.golf/catalan-numbers#python
# wren 20230304

# Catalan’s constant is a mathematical constant equal to 1/1 − 1/3² + 1/5² − 1/7² + 1/9² − …
# It is unrelated to the Catalan numbers except by name.
# Print Catalan’s constant to the first 1,000 decimal places. 

# https://en.wikipedia.org/wiki/Catalan%27s_constant
# https://en.wikipedia.org/wiki/Dirichlet_beta_function

# because it is a function i could get the 1000th x value that should be converged to that degree

collect_catalan_sum = []
collect_catalan_sub = []

for i in range(1,1000,4):
    collect_catalan_sum.append(1/(i**2))

for i in range(3,1000,4):
    collect_catalan_sub.append(1/(i**2))

sum(collect_catalan_sum)-sum(collect_catalan_sub)

for i in range(1,1000):
    collect_catalan.append(((-1)**i)/(((2*i)+1)**2))