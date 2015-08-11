'''Problem 11 from project Euler: Largest product in a grid
https://projecteuler.net/problem=11'''


from utils import mul, slurp_file


RESULT = 70600674


def solve():
    '''Main function'''
    grid = []
    res = 0
    max_adj = 4
    text = slurp_file('p011.txt')

    for row in text.split('\n'):
        grid.append([int(x) for x in row.split(' ')])

    len_grid = len(grid)

    # Horizontal
    for i in xrange(len_grid):
        for j in xrange(len_grid - max_adj):
            res = max(res, mul([grid[i][j+x] for x in xrange(max_adj)]))

    # Vertical
    for i in xrange(len_grid):
        for j in xrange(len_grid - max_adj):
            res = max(res, mul([grid[j+x][i] for x in xrange(max_adj)]))

    # Diag 1
    for i in xrange(len_grid - max_adj):
        for j in xrange(len_grid - max_adj):
            res = max(res, mul([grid[i + x][j + x] for x in xrange(max_adj)]))

    # Diag 2
    for i in xrange(max_adj - 1, len_grid - max_adj):
        for j in xrange(len_grid - max_adj):
            res = max(res, mul([grid[i - x][j + x] for x in xrange(max_adj)]))

    return res

if __name__ == '__main__':
    print solve()
