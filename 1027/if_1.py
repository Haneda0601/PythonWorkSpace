while True:
    str = input("好きな文字を入力してください：")

    if str == "":
        break
    elif str.isdigit():
        print("数字")
    elif str.isalpha():
        print("アルファベット")
    else:
        print("その他")