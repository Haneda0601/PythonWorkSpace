words = []
dic = {}

with open("./1117/data/word_list.txt", mode='r') as f:
    words = f.read().splitlines()
f.close()

for l in words:
    if l in dic:
        dic[l] = str(int(dic.get(l,0)) + 1)
    else:
        dic[l] = "1"

dic = sorted(dic.items())
for d in dic:
    print(f"{d[0]:<14}:{d[1]}")
