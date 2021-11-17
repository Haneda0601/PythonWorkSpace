def list2int(s):
    """list2int 文字列を数値に変換した値を返す（List 対応）"""
    temp = []

    if isinstance(s, list):
        for l in s:
            try:
                temp.append(int(l))
            except:
                temp.append(0)
        return temp
    else:
        try:
            return int(s)
        except:
            return 0


print(list2int(['5', 'ab', '100', 10, 1]))
print(list2int('100'))
print(list2int('xyz'))
