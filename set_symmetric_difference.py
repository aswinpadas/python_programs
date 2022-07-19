# Hacker Rank set => Symmetric Difference solution

a_size, a = (int(input()), set(map(int, input().split())))
b_size, b = (int(input()), set(map(int, input().split())))
print(*sorted(list(set(a - b).union(b - a))), sep="\n")
