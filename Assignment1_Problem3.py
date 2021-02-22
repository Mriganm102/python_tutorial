def account(year_invested):
    first = 19500
    second = 6000
    third = 25500
    import random
    percent = random.randint(-5, 5)
    percent = percent/100
    money1 = []
    money = 0
    for i in range(0, year_invested):
        money = first + money
        money = 1.07 * money
        money3 = money * percent
        money = money + money3
        money = round(money, 2)
        money1.append(money)
    print(money1)
    import matplotlib.pyplot as mat
    mat.plot(money1)
    mat.show()
account(43)

print("If input is 19500, output is 5,169,856.68")
print("If input is 6000, output is 1,590,725.18")
print("If input is 25500, output is 6,760,581.87")


