# Hacker Rank String => Capitalize solution

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    return "".join([str(x).capitalize() for x in s.split(" ")])
    # another method  : return ' '.join(map(str.capitalize, s.split(' ')))


if __name__ == '__main__':
    fptr = open("./result.output", 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
