# Hacker Rank String => Mutations


def mutate_string(string, position, character):
    string[position] = character
    return "".join(string)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(list(s), int(i), c)
    print(s_new)