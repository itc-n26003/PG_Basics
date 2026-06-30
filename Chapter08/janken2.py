import random

# コンピュータの手
computer = random.randint(1, 3)

# プレイヤーの入力
player = input("グー＝１、チョキ＝２、パー＝３: ")

# 入力を数字に変換
if player == "1" or player == "グー":
    player = 1
elif player == "2" or player == "チョキ":
    player = 2
elif player == "3" or player == "パー":
    player = 3
else:
    print("入力が正しくありません")
    exit()

# 手の表示
hand = {1: "グー", 2: "チョキ", 3: "パー"}

print("あなた:", hand[player])
print("コンピュータ:", hand[computer])

# 勝敗判定
if player == computer:
    print("あいこです")
elif (player == 1 and computer == 2) or \
     (player == 2 and computer == 3) or \
     (player == 3 and computer == 1):
    print("あなたの勝ちです！")
else:
    print("あなたの負けです")
