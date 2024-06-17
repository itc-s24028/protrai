# s24028 def4.py
# ランダムでおみくじを出すヤツ

import random
def omikuji():
    kuji=["大吉","中吉","吉","小吉","凶"]
    return random.choice(kuji)

kekka = omikuji()
print(f"結果は {kekka} です")