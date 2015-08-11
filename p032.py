'''Problem 32 from project Euler: Pandigital products
https://projecteuler.net/problem=32'''


RESULT = 45228


def solve():
    '''Main function'''

    pandigitals = set()

    for mul_a in xrange(10000):
        for mul_b in xrange(10000):
            prod = mul_a * mul_b
            tmp = ''.join([str(mul_a), str(mul_b), str(prod)])

            len_tmp = len(tmp)

            if len_tmp > 9:
                break

            if len(tmp) == 9 and ''.join(sorted(tmp)) == '123456789':
                pandigitals.add(prod)

    return sum(pandigitals)

if __name__ == '__main__':
    print solve()
