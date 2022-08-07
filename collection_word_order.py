"""Hacker Rank : Collections Word Order solution"""

import collections

words = collections.Counter([input() for _ in range(int(input()))])
print(len(words))
print(*words.values())
