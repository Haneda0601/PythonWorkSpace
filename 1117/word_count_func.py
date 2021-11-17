import re

with open("./1117/data/sentence.txt", mode='r') as f:
    sentence = f.read()
f.close()

dic = {}

sentence = re.sub('[,."()]',"",sentence)
sentence = re.sub('[:\n]'," ",sentence)
sentence = sentence.lower()
sentence = sentence.split(' ')

print(sentence)

for l in sentence:
    if l in dic:
        dic[l] = str(int(dic.get(l,0)) + 1)
    else:
        dic[l] = "1"

dic = sorted(dic.items())
for d in dic:
    print(f"{d[0]:<14}:{d[1]}")
