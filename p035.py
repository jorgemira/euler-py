'''Problem 35 from project Euler: Circular primes
https://projecteuler.net/problem=35'''


from utils import is_prime


RESULT = 55


def get_rotations(num):
    '''Returns a list with the rotations of a given number'''

    result = set()
    result.add(num)
    str_num = str(num)

    for _ in xrange(len(str(num)) - 1):
        str_num = str_num[1:] + str_num[:1]
        result.add(int(str_num))

    return result


def all_odd(num):
    '''Checks wether all the digits of a number are odd or not'''

    if num == 2:
        # 2 is even but prime
        return True
    else:
        return all([int(x) % 2 for x in str(num)])


def solve():
    '''Main function'''

    max_nums = 1000000
    checked = set()
    result = 0

    for num in xrange(max_nums):
        rotations = get_rotations(num)
        min_rot = min(rotations)

        if not min_rot in checked:
            checked.add(min_rot)

            if all_odd(num) and all([is_prime(x) for x in rotations]):
                result += len(rotations)


    return result

if __name__ == '__main__':
    print solve()
