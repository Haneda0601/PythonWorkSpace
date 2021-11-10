import csv

csv_file = open("./1110/data/test.csv", "r", encoding="utf-8", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

sumav = [0] * 4
pc = 0
for row in f:
    if row[0] == "氏名":
        row.remove("氏名")
        print(row)
    else:
        pc+=1
        for i in range(1,5):
            sumav[i-1] += int(row[i])
for i in range(0,4):
    sumav[i] = sumav[i] / pc

print(sumav)
csv_file.close()