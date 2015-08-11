'''Problem 10 from project Euler: Summation of primes
https://projecteuler.net/problem=10'''


from utils import eratosthenes2


RESULT = 142913828922


def solve():
    '''Main function'''

    max_primes = 2000000

    return sum(eratosthenes2(max_primes))


if __name__ == '__main__':
    print solve()
