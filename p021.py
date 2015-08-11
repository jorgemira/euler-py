'''Problem 21 from project Euler: Amicable numbers
https://projecteuler.net/problem=21'''


from math import sqrt


RESULT = 31626


def sum_divs(num):
    '''Return the sum of proper divisors for a given num'''
    res = 1
    for i in xrange(2, int(sqrt(num) + 1)):
        if not num % i:
            res += i + (num/i if i != num/i else 0)
    return res


def solve():
    '''Main function'''

    amics = []
    result = 0
    max_num = 10000

    for num_a in xrange(max_num):
        num_b = sum_divs(num_a)
        amics.append(num_b)
        if (num_b < len(amics)
                and num_a != num_b
                and num_a == amics[num_b]
                and num_b == amics[num_a]):
            result += num_a + num_b

    return result

if __name__ == '__main__':
    print solve()
