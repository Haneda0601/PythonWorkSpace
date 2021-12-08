# 初期化
import random  # 乱数用モジュール
marks = ('S', 'H', 'C', 'D')  # 4 種類のマーク
cards = []  # デッキ用リスト
for m in marks:
    for n in range(1, 14):
        t = (m, n)  # タプルでカード生成
        cards.append(t)  # リストに追加
print('-'*10)
print(cards)
print('-'*10)
# 1 枚選択
r = random.randrange(52)  # 0〜51 の乱数生成
print(f'選んだカードは{cards[r]}です')
print(f'選んだカードは{random.choice(cards)}です')  # 実は 1 行で書ける

choices = []
for i in range(5):
    choices.append(random.choice(cards))
choices = sorted(choices, key=lambda x: x[1],reverse=1)

print(choices)