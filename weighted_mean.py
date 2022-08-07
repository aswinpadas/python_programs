"""Hacker Rank => 10 Days of Statistics Day 0: Weighted Mean"""

_, v, w = int(input()), list(map(int,
                                 input().rstrip().split())), list(
                                     map(int,
                                         input().rstrip().split()))

print(round((sum([i * j for i, j in zip(v, w)]) / sum(w)), 1))
