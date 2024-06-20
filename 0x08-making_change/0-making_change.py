#!/usr/bin/python3
"""
Change making module. This module provides a function to
determine the fewest number of coins needed to meet a given
amount total when given a pile of coins of different values.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a
    given amount total.

    Args:
        coins (list): A list of coin values.
        total (int): The total amount of money to make change for.

    Returns:
        int: The fewest number of coins needed to meet the
             total. Returns -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    try:
        rem = total
        coins_count = 0
        coin_idx = 0
        sorted_coins = sorted(coins, reverse=True)
        n = len(coins)

        while rem > 0:
            if coin_idx >= n:
                return -1
            if rem - sorted_coins[coin_idx] >= 0:
                rem -= sorted_coins[coin_idx]
                coins_count += 1
            else:
                coin_idx += 1

        return coins_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
