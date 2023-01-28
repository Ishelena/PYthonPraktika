price = 0
ticket = int(input("Введите кол-во билетов: "))
for i in range(1, ticket + 1):
    age = int(input("Введите возраст участника: "))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    else:
        price += 1390
        pass
if ticket >= 3:
    price = price - price * 0.1
print("Сумма к оплате: ", price)




