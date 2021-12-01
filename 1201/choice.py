def odd():
    print("奇数")


def even():
    print("偶数")


def choice_func(number):
    if int(number) % 2 == 0:
        func = even()
    else:
        func = odd()
    return func


# main
while True:
    num = input("数字を入力してください。（0：終了）")
    if num.isdigit():
        if int(num) != 0:
            choice_func(num)
        else:
            break
    else:
        print("入力が正しくありません。")