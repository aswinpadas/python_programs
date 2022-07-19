# Hacker Rank Collection => Collecion Counter soutions

from collections import Counter
from itertools import count

n = int(input())
available_sizes = Counter(list(map(int, input().split()))[:n])
purchase_amt = 0
for x in range(0, int(input())):
    size, rate = input().split()
    if available_sizes[int(size)] != None and available_sizes[int(size)] != 0:
        available_sizes[int(size)] -= 1
        purchase_amt += int(rate)
print(purchase_amt)
