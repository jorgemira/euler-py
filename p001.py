'''Problem 1 from project Euler: Multiples of 3 and 5
https://projecteuler.net/problem=1'''


RESULT = 233168


def solve():
    '''Main function'''

    max_num = 1000
    return sum([x for x in xrange(max_num) if x % 3 == 0 or x % 5 == 0])

if __name__ == '__main__':
    print solve()
