'''Problem 12 from project Euler: Highly divisible triangular number
https://projecteuler.net/problem=12'''


from math import sqrt


RESULT = 76576500


def num_divs(num):
    '''Returns the number of divisors of a given number'''

    middle = sqrt(num)
    divs = 1 if middle == int(middle) else 2

    for div in xrange(2, int(middle) + 1):
        if not num % div:
            divs += 2

    return divs


def triangulars():
    '''Generator that returns triangular numbers'''

    triangular = 1
    count = 1

    while True:
        yield triangular
        count += 1
        triangular += count


def solve():
    '''Main function'''

    result = 0
    max_divisors = 500

    for num in triangulars():
        if num_divs(num) > max_divisors:
            result = num
            break

    return result

if __name__ == '__main__':
    print solve()
