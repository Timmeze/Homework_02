from app.lib import bonus_count

buy_sum1 = int(input('Введите сумму покупки '))
acc_sum1 = int(input('Введите накопленную сумму на карте'))
print(bonus_count(buy_sum1, acc_sum1))
