'''Problem 15 from project Euler: Lattice paths
https://projecteuler.net/problem=15'''


from math import factorial


RESULT = 137846528820


def solve():
    '''Main function'''

    size = 20
    result = factorial(size * 2) / factorial(size)**2

    return result

if __name__ == '__main__':
    print solve()
