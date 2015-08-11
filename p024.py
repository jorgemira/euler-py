'''Problem 24 from project Euler: Lexicographic permutations
https://projecteuler.net/problem=24'''


from utils import mul


RESULT = 2783915460


def solve():
    '''Main function'''
    top = 10
    nth = 1000000

    nth -= 1
    nums = range(top)
    res = ""

    for i in reversed(xrange(top)):
        tmp = mul(xrange(1, i+1))
        res += str(nums.pop(nth/tmp))
        nth %= tmp

    return int(res)

if __name__ == '__main__':
    print solve()
