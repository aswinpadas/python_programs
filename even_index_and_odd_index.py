""" Hacker rank 30 Days of CodeDay 6: Lets Review """
"""
Task: 
    Given a string, S, of length N that is indexed from 0 to N - 1, print its 
    even-indexed and odd-indexed characters as  space-separated strings on a 
    single line (see the Sample below for more detail).
"""

testcases = [input() for _ in range(int(input()))]
print(*[x[0::2] + " " + x[1::2] for x in testcases], sep="\n")
