# s = 'chcshdcsdcvcgvagc'
# print("".join(sorted(list(s))))

# a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

# print(*["".join(sorted(list(s)))[i:i + 4] for i in range(0, len(s), 4)], )

# import decimal

# n = 17
# print(decimal.Decimal(17))

# number = 17
# print([
#     x + '\t' + (oct(x)[2:] + '\t' + hex(x).upper()[2:] + '\t' + bin(x)[2:])
#     for x in range(1, 18)
# ])

# print(*[
#     x + '\t' + (oct(x)[2:] + '\t' + hex(x).upper()[2:] + '\t' + bin(x)[2:])
#     for x in range(1, 18)
# ],
#       sep='\n')
# number = 17
# print('\n'.join(" ".join([str(x).rjust(len(format(number, 'b'))),format(x, 'o').rjust(len(format(number, 'b'))),format(x, 'X').rjust(len(format(number, 'b'))),format(x, 'b').rjust(len(format(number, 'b')))]) for x in range(1, number + 1)))

# def print_formatted(number):
#     # your code goes here
#     return '\n'.join(
#         "\t".join([str(x) + format(x, 'o') + format(x, 'X') + format(x, 'b')])
#         for x in range(1, number + 1))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# s = 'christy saji'
# print(''.join(str(x[0].upper() + x[1:] + ' ') for x in [j for j in s.split(" ")]))

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the solve function below.
# s = '1 w 2 r 3g'
# #print(" ".join([str(x).capitalize() for x in s.split(" ")]))
# print(' '.join(map(str.capitalize, s.split(' '))))
# from itertools import product

# A = [1, 2]
# B = [3, 4]

# print(" ".join((str(x)) for x in (product(A, B))))

# print(*list(
#     map("".join,
#         list(combinations(sorted(word), int(x))
#              for x in range(1, len(word))))),
#       sep="\n")

# import itertools

# s = input().split()
# string, number = sorted(s[0]), int(s[1])
# for i in range(1, number + 1):
#     print(*list(map(''.join, itertools.combinations(string, i))), sep='\n')
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# print()
# a_size, a = (int(input()), set(map(int, input().split())))
# b_size, b = (int(input()), set(map(int, input().split())))
# print(*sorted(list(set(a - b).union(b - a))), sep="\n")

# import textwrap

# print(*[x.split("\n") for x in [textwrap.fill("aabbccdd", 2)]])

# def increment(j):
#     j = [i + 1 for i in j]
#     print("j in function after increment : ", j)

# j = [5, 6, 7]
# j
# print("j before increment : ", j)
# increment(j)
# print("j after increment : ", j)

# def double(bonus):
#     return bonus * 2

# # bonuses = [100, 200, 300]

# # iterator = list(map(double, bonuses))
# # print(iterator)
# # print(bonuses)

# # s = {11: 121, 2: 4, 3: 9, 5: 25, 7: 49}
# # print(s)
# # print(*{x for x in s.items()})

# def increment(j):
#     j = [i + 1 for i in j]
#     print("j in function after increment : ", j)

# j = [5, 6, 7]
# print("j before append : ", j)
# k = j
# print(id(j), id(k))
# k.append(8)
# print("k after append : ", k)
# print("j after append : ", j)


def test(x):
    print(x)


p = "helloi"
q = "hello"
print(id(p[0]), id(q[0]))
print(id(p), id(q))
test(id(p))
