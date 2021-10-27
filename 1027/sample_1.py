while True:
    n = input("整数を入力して下さい（終了-> 0）:")
    if int(n) == 0:
        break
    elif int(n) % 2 == 0:
        print("偶数です")
    else:
        print("奇数です")
