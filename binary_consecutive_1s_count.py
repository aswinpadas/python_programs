"""Hacker Rank 30 Days of Code Day 10: Binary Numbers"""
"""maximum number of consecutive 1's  i  the binary"""

print(max([len(x) for x in "{0:b}".format(int(input())).split("0")]))