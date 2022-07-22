# Hacker Rank itertools => Maximize it! Solutions

#not completed

km = list(map(int, input().split()))
sum = 0
s = (list(map(int, input().split()))[1:] for _ in range(km[0]))
print(*[[x**2 % km[1] for x in i] for i in s])

# for _ in range(km[0]):
#     max_of_list = max(list(map(int, input().split())))
#     sq_max_of_list = max_of_list**2
#     print('max of list = ', max_of_list, '; sq = ', sq_max_of_list)
#     sum += sq_max_of_list
# #     print('sum = ', sum)
# print(max(sum % km[1]))

from itertools import product

k, m = map(int, input().split())
n = (list(map(int, input().split()))[1:] for _ in range(k))
# print(list(product(n)))
results = map(lambda x: sum(i**2 for i in x) % m, product(*n))
print(list(results))
print(max(results))
