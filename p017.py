'''Problem 17 from project Euler: Number letter counts
https://projecteuler.net/problem=17'''


VALS = {0: 0,
        1: len('one'),
        2: len('two'),
        3: len('three'),
        4: len('four'),
        5: len('five'),
        6: len('six'),
        7: len('seven'),
        8: len('eight'),
        9: len('nine'),
        10: len('ten'),
        11: len('eleven'),
        12: len('twelve'),
        13: len('thirteen'),
        14: len('fourteen'),
        15: len('fifteen'),
        16: len('sixteen'),
        17: len('seventeen'),
        18: len('eighteen'),
        19: len('nineteen'),
        20: len('twenty'),
        30: len('thirty'),
        40: len('forty'),
        50: len('fifty'),
        60: len('sixty'),
        70: len('seventy'),
        80: len('eighty'),
        90: len('ninety'),
        100: len('hundred'),
        1000: len('thousand')}
RESULT = 21124


def lenwords(num):
    '''Return the number of letters used in writting a given number in
    English'''

    count = 0
    if num / 1000:
        return VALS[num/1000] + VALS[1000]

    if num / 100:
        count += VALS[num/100] + VALS[100]
        if num % 100:
            count += 3
        num %= 100

    if num in VALS:
        count += VALS[num]
    else:
        count += VALS[num - (num % 10)] + VALS[num % 10]

    return count


def solve():
    '''Main function'''

    max_number = 1000

    return sum([lenwords(x) for x in xrange(1, max_number + 1)])

if __name__ == '__main__':
    print solve()
