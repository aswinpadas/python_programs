# Hacker Rank string => String Validators solution

if __name__ == '__main__':
    s = list(input())

    print(any([item.isalnum() for item in s]))
    print(any([item.isalpha() for item in s]))
    print(any([item.isdigit() for item in s]))
    print(any([item.islower() for item in s]))
    print(any([item.isupper() for item in s]))
    print('\n\n**************************\n\n')

    # another method : for future references
    for method in [
            str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper
    ]:
        print(any(method(c) for c in s))