def do_anything(*args):
    '''引数の個数によって何かする。int と str で動作'''
    print(f"受け取った値:{args}")
    if len(args) == 0:
        print("やること無いので暇です")
    if len(args) == 1:
        if str(args[0]).isalnum():
            print(args[0] * 2)
        else:
            print("難しくて無理です")
    if len(args) == 2:
        if str(args[0]).isalnum() and str(args[1]).isalnum():
            try:
                print(args[0] + args[1])
            except:
                print("できません～")
        else:
            print("無茶言わないで！")
    if len(args) == 3:
        print("無理です...")

# main
do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1, 2, 3])
do_anything(10, 20)
do_anything(10, 'abc')
do_anything(10, [1, 2, 3])
do_anything(10, [1, 2, 3], 20)

