salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев




# применяем цикл for, т.к. число шагов известно

for i in range(0, 10):
    spend += spend * 0.03
    need_money += spend - salary



print(round(need_money))
# не понимаю, где ошибка :(
