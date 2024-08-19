# s24028 def4_kadai.py
# ランダムでおみくじを出すヤツ

import random

def main():
    kuji=["大吉","中吉","吉","小吉","凶"]
    kekka = random.choice(kuji)
    print(f"結果は {kekka} です")

if __name__ == '__main__':
    main()