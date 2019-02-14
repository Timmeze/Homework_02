def bonus_count(buy_sum, acc_sum):
    if buy_sum + acc_sum < 15_001:
        bonus = (buy_sum % 1000 + acc_sum)// 1000 * 50
    if 15_000 <= buy_sum + acc_sum < 150_001:
        bonus = (buy_sum % 1000 + acc_sum) // 1000 * 70
    if buy_sum + acc_sum >= 150_001:
        bonus = (buy_sum % 1000 + acc_sum) // 1000 * 100
    return bonus

print(bonus_count(1970, 1230))
