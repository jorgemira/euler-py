'''Problem 6 from project Euler: Sum square difference
https://projecteuler.net/problem=6'''


RESULT = 25164150


def solve():
    '''Main function'''

    max_num = 100

    square_of_sum = sum(xrange(1, max_num + 1))**2
    sum_of_squares = sum([x*x for x in xrange(1, max_num + 1)])

    return square_of_sum - sum_of_squares

if __name__ == '__main__':
    print solve()
