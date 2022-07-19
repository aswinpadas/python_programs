# Hacker Rank Set => Introduction  to set solution
def average(array):
    # your code goes here
    return sum(s for s in set(array)) / len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)