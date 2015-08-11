'''Problem 4 from project Euler: Largest palindrome product
https://projecteuler.net/problem=4'''


RESULT = 906609


def solve():
    '''Main function'''

    result = 0
    max_num = 1000

    for num1 in reversed(xrange(100, max_num)):
        for num2 in reversed(xrange(100, max_num)):
            if num1 * num2 > result:
                val = str(num1 * num2)
                if val == val[::-1]:
                    result = num1*num2
            else:
                break

    return result

if __name__ == '__main__':
    print solve()
