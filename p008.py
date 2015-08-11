'''Problem 8 from project Euler: Largest product in a series
https://projecteuler.net/problem=8'''


from utils import mul, slurp_file


RESULT = 23514624000


def solve():
    '''Main function'''

    num = slurp_file('p008.txt').replace('\n', '')

    adj_n = 13
    max_total = 0

    for i in xrange(len(num) - (adj_n - 1)):
        total = mul([int(x) for x in num[i: i + adj_n]])
        max_total = max(max_total, total)

    return max_total


if __name__ == '__main__':
    print solve()
