import os

words = []

if not(os.path.exists('./1103/data/sample.txt')):
    open("./1103/data/sample.txt", mode='w', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

with open("./1103/data/sample.txt", mode='r') as f:
    words = f.read().splitlines()
f.close()

while True:
    f = input("単語を入力してください：")
    if f == "":
        print("終了します")
        break
    elif f == "LIST":
        print(f"単語リスト：{words}")
    elif f in words:
        print("既に登録済です")
    else:
        words.append(f)
print(f"これまでに覚えた単語：{words}")

file = open('./1103/data/sample.txt','w')
for w in words:
    file.write(w+"\n")
file.close()