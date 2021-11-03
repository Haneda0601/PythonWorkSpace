import csv

csv_file = open("./1103/data/test.csv", "r", encoding="utf-8", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

sums = 0
for row in f:
    if row[0] == "氏名":
        continue
    for i in range(1,5):
        sums += int(row[i])
    print(f"{row[0]} {sums}")
    sums = 0

csv_file.close()