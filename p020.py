'''Problem 20 from project Euler: Factorial digit sum
https://projecteuler.net/problem=20'''


from math import factorial


RESULT = 648


def solve():
    '''Main function'''

    max_fact = 100

    return sum([int(x) for x in str(factorial(max_fact))])

if __name__ == '__main__':
    print solve()
