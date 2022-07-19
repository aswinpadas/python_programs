# Hacker Rank Sets => The Captain's Room solution

# my method :
import collections

from collections import Counter

_, a = (int(input()), dict(Counter(list(map(int, input().split())))))
print(*[x for x, y in a.items() if y == 1])

# this method too much time. so change  -->
# _, a = (int(input()), dict(Counter(list(map(int, input().split())))))
# print(*[x for x in set(a) if a.count(x)==1])

#_____________________________________________________________________________________
#another method :
# k, arr = int(input()), list(map(int, input().split()))

# myset = set(arr)

# print(((sum(myset) * k) - (sum(arr))) // (k - 1))
