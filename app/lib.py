def bonus_count(buy_sum, acc_sum):
    """
    >>> bonus_count(0, 0)
    0
    >>> bonus_count(1100, 900)
    100
    >>> bonus_count(10_000, 5_001)
    700
    >>> bonus_count(100_000, 5_0001)
    10_000
    """
    if buy_sum + acc_sum < 15_001:
        bonus = (buy_sum % 1000 + acc_sum)// 1000 * 50
    if 15_000 <= buy_sum + acc_sum < 150_001:
        bonus = (buy_sum % 1000 + acc_sum) // 1000 * 70
    if buy_sum + acc_sum >= 150_001:
        bonus = (buy_sum % 1000 + acc_sum) // 1000 * 100
    return bonus


