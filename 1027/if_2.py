while True:
    str = input("好きな文字を入力してください：")

    if str == "":
        break
    elif str.isalnum():
        if str.isdigit():
            print("数字")
            continue
        elif str.isalpha():
            print("アルファベット")
            continue
        print("アルファベットと数字")
    else:
        print("その他")
