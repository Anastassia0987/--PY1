money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


spend += spend * 0.05
money_capital -= spend
month += 1
for i in [month, month + 1]:
    if money_capital >= salary - spend:
        month += 1

print(month)
