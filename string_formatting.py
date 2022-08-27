# Hacker Rank String => String formatting solution
number = int(input())
print('\n'.join(" ".join([
    str(x).rjust(len(format(number, 'b'))),
    format(x, 'o').rjust(len(format(number, 'b'))),
    format(x, 'X').rjust(len(format(number, 'b'))),
    format(x, 'b').rjust(len(format(number, 'b')))
]) for x in range(1, number + 1)))