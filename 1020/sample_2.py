fruits = ['バナナ','リンゴ','オレンジ']
while True:
    f = input("果物をカタカナで入力してください：")
    if f == "":
        break
    elif f in fruits:
        print(f"{f}は知っています！")
    else:
        print(f"{f}は知りませんでした。覚えておきます。")
        fruits.append(f)
print('知っている果物')
print(fruits)