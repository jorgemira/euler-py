'''Problem 28 from project Euler: Number spiral diagonals
https://projecteuler.net/problem=28'''


RESULT = 669171001


def solve():
    '''Main function'''

    total = 1
    max_num = 1001
    limit = ((max_num - 1) / 2) + 1

    for i in xrange(1, limit):
        num = 2*i + 1
        total += 4*(num**2) - 6*(num-1)

    return total

if __name__ == '__main__':
    print solve()
