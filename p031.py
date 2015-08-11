'''Problem 31 from project Euler: Coin sums
https://projecteuler.net/problem=31'''


RESULT = 73682


def num_ways(amount, coins):
    '''Returns the number of ways that a given amount can be made with a given
    set of coins'''

    ways = 0

    if amount:
        if coins:
            max_coin = coins[0]
            if amount >= max_coin:
                ways += num_ways(amount - max_coin, coins)
            ways += num_ways(amount, coins[1:])
        return ways
    else:
        return 1


def solve():
    '''Main function'''

    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    amount = 200

    return num_ways(amount, coins)

if __name__ == '__main__':
    print solve()
