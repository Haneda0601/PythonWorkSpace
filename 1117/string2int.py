def str2int(s):
    """str2int 文字列を数値に変換した値を返す"""
    try:
        return int(s)
    except:
        return 0

print(str2int('a'))
print(str2int('10'))
print(str2int(100))
