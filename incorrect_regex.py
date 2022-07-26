"""
Haker Rank Exception and Errors => Incorrect Regex soulution
"""

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
