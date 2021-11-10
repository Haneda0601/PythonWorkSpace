import pickle
import os

words = []

if os.path.exists('./1110/data/testwords.pkl'):
    with open('./1110/data/testwords.pkl', 'rb') as f:
        words = pickle.load(f)


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

with open('./1110/data/testwords.pkl', 'wb') as f:
    pickle.dump(words, f)