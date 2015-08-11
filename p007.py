'''Problem 7 from project Euler: 10001st prime
https://projecteuler.net/problem=7'''


from utils import is_prime


RESULT = 104743


def solve():
    '''Main function'''

    count = 0
    num = 1
    nth_num = 10001

    while count < nth_num:
        num += 1
        if is_prime(num):
            count += 1

    return num

if __name__ == '__main__':
    print solve()
