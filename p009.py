'''Problem 9 from project Euler: Special Pythagorean triplet
https://projecteuler.net/problem=9'''


RESULT = 31875000


def solve():
    '''Main function'''

    total = 1000

    for num_a in xrange(1, 251):
        num_b = num_a + 1
        while num_b < (total - num_a - num_b):
            num_c = total - num_a - num_b
            if num_a**2 + num_b**2 == num_c**2:
                return num_a * num_b * num_c
            num_b += 1

if __name__ == '__main__':
    print solve()
