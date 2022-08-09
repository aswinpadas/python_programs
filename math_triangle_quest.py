""" Hacker rank : Math Triangle Quest Solution """

for x in range(0, int(input()) - 1):
    print([1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][x])

# another Method: Some real Math

for x in range(1, int(input())):
    print((10**(x) // 9) * x)
