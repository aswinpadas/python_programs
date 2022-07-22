#!/bin/python3

import math
import datetime
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    # print(datetime.datetime.strptime(*t1))
    pass


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input().split()

        t2 = input().split()
        print(
            datetime.datetime.strptime(*t1) - datetime.datetime.strptime(*t2))

        delta = time_delta(t1, t2)
