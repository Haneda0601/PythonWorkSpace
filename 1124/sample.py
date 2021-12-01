while(True):
    i = input("整数を入力してください（終了->0）：")
    if int(i) == 0:break
    elif int(i) % 2 == 0:print("偶数です。") 
    else:print("奇数です。")
