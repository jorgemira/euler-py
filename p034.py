'''Problem 34 from project Euler: Digit factorials
https://projecteuler.net/problem=34'''


from math import factorial


FACTS = [factorial(n) for n in xrange(10)]
RESULT = 40730


def get_digits(num):
    '''Generator that yields the digits of a number'''

    while num:
        yield num % 10
        num /= 10


def is_curious(num):
    '''Return True if a number is equal to the sum of the factorials of its
    digits, false otherwise'''

    return num == sum([FACTS[x] for x in get_digits(num)])


def get_limit():
    '''Return the upper limit for the problem'''

    count = 1

    while 10 ** count < count * FACTS[9]:
        count += 1

    return FACTS[9] * count


def solve():
    '''Main function'''

    total = 0
    limit = get_limit()

    for num in xrange(10, limit):
        if is_curious(num):
            total += num

    return total


if __name__ == "__main__":
    print solve()
