'''Problem 23 from project Euler: Non-abundant sums
https://projecteuler.net/problem=23'''


from utils import divisors


RESULT = 4179871


def solve():
    '''Main function'''

    all_sums = set()
    limit = 28123
    abundants = [n for n in xrange(1, limit) if sum(divisors(n)) > n]

    for i in abundants:
        for j in abundants:
            if i+j < limit:
                all_sums.add(i+j)
            else:
                break

    return sum(xrange(1, limit)) - sum(all_sums)

if __name__ == '__main__':
    print solve()
