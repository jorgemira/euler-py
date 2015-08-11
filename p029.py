'''Problem 29 from project Euler: Distinct powers
https://projecteuler.net/problem=29'''


RESULT = 9183


def solve():
    '''Main function'''
    vals = set()
    limit = 100

    for i in xrange(2, limit + 1):
        for j in xrange(2, limit + 1):
            vals.add(i**j)

    return len(vals)

if __name__ == '__main__':
    print solve()
