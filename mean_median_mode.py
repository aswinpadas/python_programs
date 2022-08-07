"""Imp : Hacker Rank : 10 Days of Statistics Day 0: Mean, Median, and Mode Solution"""

import collections

_, values = input(), sorted(list(map(int, input().split())))
length = len(values)
print("{:.1f}".format(sum(values) / len(values)))
print((values[int(length / 2) - 1] + values[int(length / 2)]) / 2)
values = collections.Counter(values)
print(values.most_common()[0][0])
