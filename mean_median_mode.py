"""Imp : Hacker Rank : 10 Days of Statistics Day 0: Mean, Median, and Mode Solution"""

import collections

_, values = input(), sorted(list(map(int, input().split())))
length = len(values)
print("{:.1f}".format(sum(values) / len(values)))
print((values[int(length / 2) - 1] + values[int(length / 2)]) / 2)
values = collections.Counter(values)
print(values.most_common()[0][0])
""" Solution using Numpy"""

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))