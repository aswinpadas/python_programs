# Hacker Rank Set => Mutations solution

_, a = (int(input()), set(map(int, input().split())))
for x in range(0, int(input())):
    operation_name, b = (input().split()[0], set(map(int, input().split())))
    getattr(a, operation_name)(b)
print(sum(a))
