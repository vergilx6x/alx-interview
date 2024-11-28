#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given total."""
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coins_count, rem = 0, total

    for coin in sorted_coins:
        while rem >= coin:
            rem -= coin
            coins_count += 1

    return coins_count if rem == 0 else -1
