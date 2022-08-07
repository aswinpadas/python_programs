"""Imp Hacker rank : Collections.OrderedDict() solution

"""

from collections import OrderedDict

ord_dict = OrderedDict()

for x in [input().split(" ") for _ in range(int(input()))]:
    ord_dict[" ".join(x[0:len(x) - 1])] = ord_dict.get(
        " ".join(x[0:len(x) - 1]), 0) + int(x[len(x) - 1])
print(*[" ".join([i, str(j)]) for i, j in ord_dict.items()], sep="\n")