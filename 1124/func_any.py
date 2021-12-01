def out_csvdata(**kwargs):
    '''記録された食事の内容を出力'''
    menu = []
    for i in ['B', 'L', 'D']:
        if i in kwargs.keys():
            menu.append(kwargs[i])
        else:
            menu.append('-')
    print(menu)

# main
eat = {}

while True:
    menu = input("朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：")
    if menu == '':
        break
    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        eat[token] = menu
    else:
        print('記号が間違っています。登録しません')
        continue

out_csvdata(**eat)
