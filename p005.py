'''Problem 5 from project Euler: Smallest multiple
https://projecteuler.net/problem=5'''


from fractions import gcd


RESULT = 232792560


def lcm(num1, num2):
    '''Return least common multiple of two numbers'''

    return num1 * num2 // gcd(num1, num2)


def lcmm(numbers):
    '''Return least common multiple of a list of numbers'''

    return reduce(lcm, numbers)


def solve():
    '''Main function'''

    max_num = 20

    return lcmm(xrange(1, max_num))


if __name__ == '__main__':
    print solve()
