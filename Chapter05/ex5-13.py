colors = ["purple", "orange", "green"]
guess = input("何色でしょうか？(入力てください) :")

if guess in colors:
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")
