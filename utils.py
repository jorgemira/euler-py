'''Common functions to solve Project Euler problems'''


from math import sqrt


def is_prime(num):
    '''Return whether a given number is prime or not'''

    #Handle special cases first
    if num < 2:
        return False

    if num == 2:
        return True

    if not num % 2:
        return False

    mid = int(sqrt(num)) + 1

    for count in xrange(3, mid, 2):
        if not num % count:
            return False

    return True


def prime_factors(num):
    '''Return a list with the prime factors of num'''

    result = []
    count = 2
    limit = sqrt(num)

    while num != 1 or count < limit:
        if not num % count:
            result.append(count)
            while not num % count:
                num /= count
            limit = sqrt(num)
        count += 1

    return result


def eratosthenes2(max_num):
    '''Return an array with the primes up to max_num'''

    multiples = set()
    result = []
    for i in xrange(2, max_num+1):
        if i not in multiples:
            result.append(i)
            multiples.update(xrange(i*i, max_num+1, i))

    return result


def mul(values):
    '''Return the result of multipliying all elements of a list'''

    if len(values):
        return reduce(lambda x, y: x * y, values)
    else:
        return 1


def slurp_file(fname):
    '''Return a string with the content of a file'''

    with open(fname) as my_file:
        text = my_file.read().rstrip()

    return text


def divisors(num):
    '''Return a list with the divisors of the given number'''
    divs = [1]

    for i in xrange(2, int(sqrt(num) + 1)):
        if not num % i:
            divs.append(i)
            if i != num/i:
                divs.append(num/i)
    return divs


def solve_triangle(filename):
    '''Solves the triangle problem from problems 18 and 67'''

    grid = []
    text = slurp_file(filename)

    for row in text.split('\n'):
        grid.append([int(x) for x in row.split(' ')])

    prev_line = grid[-1]

    for i in reversed(xrange(len(grid)-1)):
        line = []
        for j in xrange(i+1):
            line.append(grid[i][j] + max(prev_line[j], prev_line[j+1]))
        prev_line = line

    return line[0]


def static_vars(**kwargs):
    '''Decorator to initialize static variables into functions'''

    def decorate(func):
        '''Creates the static variables and initializes them inside the
        given function'''

        for kwarg in kwargs:
            setattr(func, kwarg, kwargs[kwarg])

        return func

    return decorate
