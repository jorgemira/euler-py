'''Problem 14 from project Euler: Longest Collatz sequence
https://projecteuler.net/problem=14'''


from utils import static_vars


RESULT = 837799


@static_vars(seqs = {1: 1})
def collatz(num):
    '''Returns the number of terms for a given num for the Collatz sequence'''
    if not num in collatz.seqs:
        collatz.seqs[num] = 1 + collatz(3 * num + 1 if num % 2 else num / 2)
    return collatz.seqs[num]


def solve():
    '''Main function'''

    n_max = 0
    res = 0
    max_collatz = 1000000

    for i in xrange(1, max_collatz):
        seq = collatz(i)
        if seq > res:
            n_max, res = i, seq

    return n_max

if __name__ == '__main__':
    print solve()
