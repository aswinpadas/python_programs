# Hacker Rank String => Merge the Tools! soution

from collections import OrderedDict
from textwrap import fill
# single statement
print(*[
    "".join(OrderedDict.fromkeys(i))
    for i in fill(input(), int(input())).split("\n")
],
      sep=("\n"))

#-------------------------------------------------------------------------------------

#  just Wrapped in a function  :  Hacker rank default code

# from collections import OrderedDict
# from textwrap import fill

# def merge_the_tools(string, k):
#     # your code goes here
#     print(*["".join(OrderedDict.fromkeys(i)) for i in fill(string, k).split("\n")], sep=("\n"))

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)