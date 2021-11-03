with open("./1103/data/sample.txt", mode='r') as f:
    words = f.read().splitlines()

for w in words:
    print(f"{str(words.index(w) + 1).zfill(4)}:{w}")