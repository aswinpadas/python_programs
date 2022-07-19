# Hacker Rank Set => Symmetric Difference solution

a_size, a = (int(input()), set(map(int, input().split())))
b_size, b = (int(input()), set(map(int, input().split())))
print(len(a.symmetric_difference(b)))