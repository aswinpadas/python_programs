""" Hacker rank 30 Days of CodeDay 11: 2D Arrays"""
"""Calculate the hourglass sum for every hourglass in 2D array , then print the maximum hourglass sum"""

if __name__ == "__main__":
    R = 5
    C = 5

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sum = 0
    tarr = []
    list1 = []
    for l in range(0, 4):
        for k in range(0, 4):
            for i in range(l, l + 3):
                for j in range(k, k + 3):
                    if i == l + 1 and (j == k or j == k + 2):
                        continue
                    else:
                        sum += arr[i][j]
            tarr.append(sum)
            sum = 0
    print((tarr))
