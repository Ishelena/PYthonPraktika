per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете внести: "))
tkb = per_cent['ТКБ'] * money/100
skb = per_cent['СКБ'] * money/100
vtb = per_cent['ВТБ'] * money/100
sber = per_cent['СБЕР'] * money/100
deposit = [tkb, skb, vtb, sber]
print("Накопленные проценты за год: ", deposit,
      "Максимальная сумма %: ", max(deposit), "в банке: ", max(per_cent, key=per_cent.get))
