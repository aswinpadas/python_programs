# Hacker Rank Math => Polar Coordinates Solutions

import cmath
# method 1
# x = eval(input())
# print(abs(x), "\n", phase(x))

# Method 2
print(*cmath.polar(complex(input())), sep='\n')
