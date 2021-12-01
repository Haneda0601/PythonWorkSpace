# 関数を辞書で渡し、実行する
def func1():
    print("Hello")


def func2():
    print("Goodbye")


# main
run_list = {'a': func1, 'b': func2}

while True:
    sel = input("a=>Hello,b=>GoodBye\nどちらを実行しますか？：")
    if sel != '':
        if sel in run_list.keys():
            run_list[sel]()
        else:
            print("どちらかを選択して下さい。")
    else:
        break
