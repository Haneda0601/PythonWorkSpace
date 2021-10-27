# 初期化
marks = ('S','H','C','D') # 4 種類のマーク
cards = [] # デッキ用リスト
for mark in marks:
    for num in range(1,14):
        cards.append((mark,num))

print('-'*10)
print(cards)
print('-'*10)
# 1 枚選択
import random # 乱数用モジュール
r = random.randrange(52) # 0〜51 の乱数生成
print(f'選んだカードは{cards[r]}です')