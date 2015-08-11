'''Problem 25 from project Euler: 1000-digit Fibonacci number
https://projecteuler.net/problem=25'''


RESULT = 4782


def solve():
    '''Main function'''

    digits = 1000
    fib1 = 1
    fib2 = 1
    nth = 2
    top = 10 ** (digits - 1)

    while fib2 < top:
        fib1, fib2 = fib2, fib1 + fib2
        nth += 1

    return nth

if __name__ == '__main__':
    print solve()
