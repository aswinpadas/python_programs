"""30 Days of CodeDay 9: Recursion 3"""


def factorial(n):

    if n == 1:
        return 1
    else:
        n = n * factorial(n - 1)
        print(n)
    return n


if __name__ == '__main__':
    fptr = open("./result.output", 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
