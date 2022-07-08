import string


def print_rangoli(size):
    alphabets = string.ascii_lowercase[:size]
    print(alphabets)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)