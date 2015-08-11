'''Problem 16 from project Euler: Power digit sum
https://projecteuler.net/problem=16'''


RESULT = 1366


def solve():
    '''Main function'''

    power = 1000

    return sum([int(x) for x in str(2**power)])

if __name__ == '__main__':
    print solve()
