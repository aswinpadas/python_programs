# Hacker Rank Iteretools => Itertoolsitertools.product()

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(" ".join(
    (str(x))
    for x in (product(A, B)
              )))  # we can use this statement while returning from a function
print(*product(A, B))  # simple method of printing
