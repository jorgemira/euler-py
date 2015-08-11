'''Problem 13 from project Euler: Large sum
https://projecteuler.net/problem=13'''


from utils import slurp_file


RESULT = 5537376230


def solve():
    '''Main function'''

    text = slurp_file('p013.txt')
    digits = 10
    total = sum([int(x) for x in text.split('\n')])

    return int(str(total)[:digits])


if __name__ == '__main__':
    print solve()
