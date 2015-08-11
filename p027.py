'''Problem 27 from project Euler: Quadratic primes
https://projecteuler.net/problem=27'''


from utils import is_prime


RESULT = -59231


def primes_exp(num_a, num_b):
    '''Returns how many consecutive primes a quadratic expression with
    coefficients num_a and num_b returns'''

    count = 1

    while is_prime(count ** 2 + num_a * count + num_b):
        count += 1

    return count


def solve():
    '''Main function'''

    max_primes = 0
    result = 0
    max_num = 1000

    for num_a in xrange(max_num):
        for num_b in xrange(max_num):

            # A B
            tmp = primes_exp(num_a, num_b)
            if max_primes < tmp:
                max_primes, result = tmp, num_a * num_b
            # A -B
            tmp = primes_exp(num_a, -num_b)
            if max_primes < tmp:
                max_primes, result = tmp, num_a * (-num_b)
            # -A B
            tmp = primes_exp(-num_a, num_b)
            if max_primes < tmp:
                max_primes, result = tmp, (-num_a) * num_b
            # -A -B
            tmp = primes_exp(-num_a, -num_b)
            if max_primes < tmp:
                max_primes, result = tmp, num_a * num_b

    return result

if __name__ == '__main__':
    print solve()
