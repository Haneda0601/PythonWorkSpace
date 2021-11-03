import time
count = input("何匹数えますか？：")

for i in range(int(count)):
    print(f"羊が{i + 1}匹")
    time.sleep((i + 1) / 4)