# Hacker Rank Itertools => itertools permutations Solutions

from itertools import permutations

word, split_length = input().split()
print(*list(map("".join, list(permutations(sorted(word), int(split_length))))),
      sep="\n")
