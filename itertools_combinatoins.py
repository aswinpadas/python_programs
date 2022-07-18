# Hacker Rank Itertools => itertools Combinations solution

from itertools import chain, combinations, permutations

word, split_length = input().split()

print(*list(
    map(
        "".join,
        list(
            chain.from_iterable(
                list(
                    list(combinations(sorted(word), x))
                    for x in range(1,
                                   int(split_length) + 1)))))),
      sep="\n")
