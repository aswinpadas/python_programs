# Hacker Rank Set => Check subset solution
for x in range(int(input())):
    _, a, _, b = (input(), set(input().split()), input(), set(input().split()))
    print(a.issubset(b))
