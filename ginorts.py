# Hacker Rank : ginortS solution

if __name__ == '__main__':
    s = sorted(list(input()))
    num = sorted([int(i) for i in s if i.isdigit()],
                 key=lambda x: (not x % 2, x))
    s = [j for j in s if j.islower()] + [j for j in s if j.isupper()] + num
    print("".join(map(str, s)))
