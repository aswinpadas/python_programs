""" Hank Rank : Built-Ins Any and All solution """

_, numlist = input(), list(map(int, input().split()))
print(
    all(
        sum([[x >= 0 for x in numlist],
             [any(str(x) == str(x)[::-1] for x in numlist)]], [])))

# Simple Solution ref.
_, numlist = input(), list(map(int, input().split()))
print(
    all(x >= 0 for x in numlist)
    and any(str(x) == str(x)[::-1] for x in numlist))
