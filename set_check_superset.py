# Hacker Rank Set => Check Superset solution

a, n_testcases = set(input().split()), int(input())
print(all([a.issuperset(set(input().split())) for _ in range(n_testcases)]))
