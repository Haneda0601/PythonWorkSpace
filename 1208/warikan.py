import math

def input_int(str):
    print(str,end='')
    return int(input())

# def calc_payment(money,people):
#     pay = math.ceil(money / (people * 100)) * 100
#     org = money - (pay * (people - 1))
#     return [pay,org,people]

# def output_payment(pay,org,people):
#     print(f"支払金額：{pay} 円 ({people - 1} 人)")
#     print(f"幹事金額：{org} 円")

#paycalc = calc_payment(input_int("支払合計金額を入力してください："),input_int("参加者人数を入力してください："))
#output_payment(paycalc[0],paycalc[1],paycalc[2])

#############################################

def calc_payment(money,people):
    pay = math.ceil(money / (people * 100)) * 100
    org = money - (pay * (people - 1))

    def output_payment(out_pay,out_org,out_people):
        print(f"支払金額：{out_pay} 円 ({out_people - 1} 人)")
        print(f"幹事金額：{out_org} 円")

    return output_payment(pay,org,people)

calc_payment(input_int("支払合計金額を入力してください："),input_int("参加者人数を入力してください："))