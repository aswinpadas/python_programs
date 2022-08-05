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

# def test(x):
#     print(x)

# p = "helloi"
# q = "hello"
# print(id(p[0]), id(q[0]))
# print(id(p), id(q))
# test(id(p))

# print(list(map(lambda x: x + 1, range(1, 10))))

# def test(x):
#     x = x + 1

# y = 2
# test(y)
# print(y)
# print("hello World\n" + input())
# print(int(input()) + 4)
# print(float(input()) + 4)
# print("HackerRank", input())

# def solve(meal_cost, tip_percent, tax_percent):
#     print(
#         round(((tip_percent / 100) * meal_cost) +
#               ((tax_percent / 100) * meal_cost) + meal_cost))

# if __name__ == '__main__':
#     meal_cost = float(input().strip())

#     tip_percent = int(input().strip())

#     tax_percent = int(input().strip())

#     solve(meal_cost, tip_percent, tax_percent)

# n = int(input())

# if n % 2 == 1:
#     print("Weird")

# else:
#     if n in range(2, 5):
#         print("Not Weird")

#     else:
#         if n in range(6, 21):
#             print("Weird")

#         else:
#             print("Not Weird")

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     print(*reversed(arr))

# if __name__ == '__main__':
#     number = int(input().strip())
#     print(*[
#         " ".join([str(number), 'x',
#                   str(count), '=',
#                   str(number * count)]) for count in range(1, 11)
#     ],
#           sep="\n")

# if __name__ == '__main__':
#     number = int(input().strip())
#     print(*[
#         "{} x {} = {}\n".format(count, number, (number * count))
#         for count in range(1, 11)
#     ],
# #           sep="\n")

# testcases = [input() for _ in range(int(input()))]
# print(*[x[0::2] + " " + x[1::2] for x in testcases], sep="\n")

# # 30 Days of CodeDay 9: Recursion 3
# def factorial(n):

#     if n == 1:
#         return 1
#     else:
#         n = n * factorial(n - 1)
#         print(n)
#     return n

# if __name__ == '__main__':
#     fptr = open("./result.output", 'w')

#     n = int(input().strip())

#     result = factorial(n)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# print(bin(int(input())).split('0b'))
# print(max([len(x) for x in "{0:b}".format(int(input())).split("0")]))
# max_sum = -50000

# if (R < 3 or C < 3):
#     print("Not possible")
#     exit()
# for i in range(0, R - 2):
#     for j in range(0, C - 2):
#         SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (
#             arr[i + 1][j + 1]) + (arr[i + 2][j] + arr[i + 2][j + 1] +
#                                   arr[i + 2][j + 2])
#         if (SUM > max_sum):
#             max_sum = SUM
#         else:
#             continue

# if __name__ == "__main__":
#     R = 5
#     C = 5

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

#     sum = 0
#     tarr = []
#     list1 = []
#     for l in range(0, 4):
#         for k in range(0, 4):
#             for i in range(l, l + 3):
#                 for j in range(k, k + 3):
#                     if i == l + 1 and (j == k or j == k + 2):
#                         continue
#                     else:
#                         sum += arr[i][j]
#             tarr.append(sum)
#             sum = 0
#     print((tarr))

# Dict range or rangfe oin dict as key
# grade = {
#     range(90, 101): "O",
#     range(80, 90): "E",
#     range(70, 80): "A",
#     range(55, 70): "P",
#     range(40, 55): "D",
#     range(0, 40): "T",
# }

# print(*[y for x, y in grade.items() if 55 in x])

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()