"""
Day 2 — Best Time to Buy and Sell Stock (LeetCode 121)

You are given an array `prices` where `prices[i]` is the price of a stock on
day `i`. Choose a single day to buy and a later day to sell to maximise profit.
Return the maximum profit, or 0 if no profit is possible.

Pattern: Single-pass array scan (track running minimum)
Time:    O(n)
Space:   O(1)

Examples:
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5
    >>> max_profit([7, 6, 4, 3, 1])
    0
"""


def max_profit(prices: list[int]) -> int:
    """Return the maximum profit from a single buy-then-sell transaction.

    Scan once: keep track of the lowest price seen so far (best buy day) and
    update the best profit whenever the current price exceeds that minimum.
    """
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        if profit > best_profit:
            best_profit = profit
        if price < min_price:
            min_price = price

    return best_profit
