'''Problem 30 from project Euler: Digit fifth powers
https://projecteuler.net/problem=30'''


RESULT = 443839


def solve():
    '''Main function'''
    res = 0
    limit = 1000000

    for i in xrange(2, limit):
        val = sum([int(x)**5 for x in str(i)])
        if i == val:
            res += i

    return res

if __name__ == '__main__':
    print solve()
