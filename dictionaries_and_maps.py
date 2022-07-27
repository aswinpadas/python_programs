"""Hacker Rank 30 Days of Code => Day 8: Dictionaries and Maps"""

tc = int(input())
ph = dict(input().split() for _ in range(tc))
while True:
    try:
        name = input()
        print(name + "=" + ph[name] if name in ph.keys() else "Not found")
    except EOFError:
        break
