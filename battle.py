# ==============================
# 寶可夢對戰（填空版）
# 目標：補上 while 條件、選項判斷、扣血/回血、勝負判定
# ==============================

player_name = "沙奈朵"
enemy_name = "快龍"

player_hp = 30
enemy_hp = 30

move1_name = "魔法葉"
move1_dmg = 8

move2_name = "精神強念"
move2_dmg = 12

potion = 2
potion_heal = 10

enemy_dmg = 6

print("道館挑戰開始！")
print(player_name, "VS", enemy_name)

turn = 1

# TODO(1) 只要雙方都還活著就繼續玩
while ____ and ____:
    print("\n" + "=" * 28)
    print("第", turn, "回合")
    print("你的HP:", player_hp, "| 對手HP:", enemy_hp)

    print("1)", move1_name, "-", move1_dmg)
    print("2)", move2_name, "-", move2_dmg)
    print("3) 用傷藥 +", potion_heal, "(剩", potion, ")")

    choice = input("選 1/2/3：").strip()

    # TODO(2) 依照 choice 做不同事（招式1/招式2/傷藥/錯誤）
    if choice == "____":
        enemy_hp = enemy_hp - ____
        print("你用了", move1_name, "！對手 -", move1_dmg)

    elif choice == "____":
        enemy_hp = enemy_hp - ____
        print("你用了", move2_name, "！對手 -", move2_dmg)

    elif choice == "____":
        # TODO(3) 傷藥還有嗎？
        if potion > ____:
            potion = potion - ____
            player_hp = player_hp + ____
            print("你用了傷藥！自己 +", potion_heal, "(剩", potion, ")")
        else:
            print("傷藥用完了，這回合沒動作。")

    else:
        print("輸入錯誤，這回合沒動作。")

    # TODO(4) 對手倒下就結束
    if enemy_hp <= ____:
        break

    # 對手固定攻擊
    player_hp = player_hp - ____
    print(enemy_name, "攻擊！你 -", enemy_dmg)

    turn = turn + ____

print("\n=== 結果判定 ===")
print("你的HP:", player_hp, "| 對手HP:", enemy_hp)

# TODO(5) 完成勝負判定
if enemy_hp <= ____ and player_hp <= ____:
    print("同歸於盡！平手！")
elif enemy_hp <= ____:
    print("你贏了！")
else:
    print("你輸了！")
