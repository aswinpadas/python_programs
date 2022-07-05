#Hacker Rank : Runner up Score Solution

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(set(map(int, input().split()))))
    print(arr[len(arr) - 2])
