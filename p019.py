'''Problem 19 from project Euler: Counting Sundays
https://projecteuler.net/problem=19'''


from datetime import datetime


RESULT = 171


def solve():
    '''Main function'''

    sundays = 0
    first = 1901
    last = 2001

    for year in xrange(first, last):
        for month in xrange(1, 13):
            date = datetime(year, month, 1)
            if date.weekday() == 6:
                sundays += 1

    return sundays

if __name__ == '__main__':
    print solve()
