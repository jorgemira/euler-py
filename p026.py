'''Problem 26 from project Euler: Reciprocal cycles
https://projecteuler.net/problem=26'''


from decimal import Decimal, getcontext


RESULT = 983


def cycle(num, prec):
    '''Return the lenght of a cycle of a given number'''

    end_loop = False
    j = 0
    while not end_loop:
        i = 3
        while not end_loop and i < prec/2:
            if num[0+j:i+j] == num[i+j:2*i+j]:
                end_loop = True
            else:
                i += 1
        j += 1
    return i


def solve():
    '''Main function'''

    prec = 2000
    getcontext().prec = prec

    max_n = 0
    max_c = 0
    max_num = 1000

    for i in reversed(xrange(2, max_num)):
        val = str(Decimal(1) / Decimal(i)).split('.')[1]
        tmp_c = cycle(val, prec)
        if tmp_c > max_c:
            max_c, max_n = tmp_c, i

    return max_n

if __name__ == '__main__':
    print solve()
