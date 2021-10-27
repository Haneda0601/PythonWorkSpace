n1 = input("数字１を入力：")
n2 = input("数字２を入力：")

print(f"{n1}から{n2}までの合計は{sum(list(range(int(n1),int(n2)+1)))}です")