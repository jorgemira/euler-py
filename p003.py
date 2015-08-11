'''Problem 3 from project Euler: Largest prime factor
https://projecteuler.net/problem=3'''


from utils import prime_factors


RESULT = 6857


def solve():
    '''Main function'''

    num = 600851475143

    return max(prime_factors(num))


if __name__ == '__main__':
    print solve()
