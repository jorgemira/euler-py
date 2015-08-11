'''Problem 22 from project Euler: Names scores
https://projecteuler.net/problem=22'''


from string import ascii_uppercase

from utils import slurp_file


RESULT = 871198282


def solve():
    '''Main function'''

    text = slurp_file('p022_names.txt')
    names = sorted(text.split(','))
    values = {x: ord(x) - 64 for x in ascii_uppercase}
    count = 0

    for i, name in enumerate(names):
        name = name.replace('"', '')
        count += (i + 1) * sum([values[x] for x in name])

    return count

if __name__ == '__main__':
    print solve()
