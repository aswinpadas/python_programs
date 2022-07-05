#Hacker Rank String => Find a string


def count_substring(string, query, count):
    idx = string.find(query)
    return count_substring(string[idx + 1:], query, count +
                           1) if idx != -1 else count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string, 0)
    print(count)