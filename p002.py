'''Problem 2 from project Euler: Even Fibonacci numbers
https://projecteuler.net/problem=2'''


RESULT = 4613732


def get_fibs(max_fib):
    '''Return next fibonacci number until it is greater than max_fib'''

    fibs = [1, 2]

    yield fibs[0]

    while fibs[-1] < max_fib:
        yield fibs[-1]

        fibs.append(fibs[-1] + fibs[-2])


def solve():
    '''Main function'''

    max_fibs = 4000000

    return sum([x for x in get_fibs(max_fibs) if not x % 2])

if __name__ == '__main__':
    print solve()
