from collections import Counter
from itertools import count

n = int(input())
available_sizes = list(map(int, input().split()))[:n]
print(available_sizes)
number_coustomers = int(input())
# purchase = [[map(int,
#                  input().split())[:2][x]] for x in range(0, number_coustomers)]
# print(purchase)
