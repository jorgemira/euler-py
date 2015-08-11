'''Problem 33 from project Euler: Digit cancelling fractions
https://projecteuler.net/problem=33'''


from fractions import gcd


RESULT = 100


def curious_fraction(num, den):
    '''Checks whether a fraction i curious or not'''

    if not num % 10 or not den % 10:
        return False

    val = num / float(den)
    (num_1, num_2) = (num / 10, num % 10)
    (den_1, den_2) = (den / 10, den % 10)

    if num_1 == den_1:
        return num_2/float(den_2) == val
    elif num_1 == den_2:
        return num_2/float(den_1) == val
    elif num_2 == den_1:
        return num_1/float(den_2) == val
    elif num_2 == den_2:
        return num_1/float(den_1) == val
    else:
        return False


def solve():
    '''Main function'''
    num_all = 1
    den_all = 1

    for den in xrange(10, 100):
        for num in xrange(10, den):
            if curious_fraction(num, den):
                num_all *= num
                den_all *= den

    return den_all / gcd(num_all, den_all)

if __name__ == "__main__":
    print solve()
