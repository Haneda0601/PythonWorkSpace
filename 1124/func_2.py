import math

def tax_included(m,tax=10):
    '''消費税が足された金額を返す'''
    if tax > 0:
        return int(m * (1 + (tax / 100)))

money = 5000

print(f"{money} の税込金額は {tax_included(money)} 円")
print(f"{money} の消費税 8%の税込金額は {tax_included(money,8)} 円")
print(f"{money} の消費税 -5%の税込金額は {tax_included(money,-5)} 円")
