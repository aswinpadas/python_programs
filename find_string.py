#Hacker Rank String => Find a string
#method 1
def count_substring(string, query, count):
    idx = string.find(query)
    return count_substring(string[idx + 1:], query, count +
                           1) if idx != -1 else count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string, 0)
    print(count)
    print(
        sum([
            1 for i in range(len(string) - len(sub_string) + 1)
            if string[i:i + len(sub_string)] == sub_string
        ]))

    print('\n\n\n\n\n')


#metheod 2
def count_substring2(string, sub_string):
    return sum([
        1 for i in range(len(string) - len(sub_string) + 1)
        if string[i:i + len(sub_string)] == sub_string
    ])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring2(string, sub_string)
    print(count)