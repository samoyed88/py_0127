# ==========================================
# 寶可夢對戰（自動充能版）填空
# ==========================================

player_name = "沙奈朵"
enemy_name = "快龍"

player_hp = 30
enemy_hp = 30

move1_name = "魔法葉"
move1_dmg = 8
move1_cost = 1

move2_name = "精神強念"
move2_dmg = 12
move2_cost = 2

enemy_move1_name = "龍爪"
enemy_move1_dmg = 7
enemy_move1_cost = 1

enemy_move2_name = "龍之波動"
enemy_move2_dmg = 11
enemy_move2_cost = 2

player_energy = 0
enemy_energy = 0

potion = 2
potion_heal = 10

print("道館挑戰開始！（自動每回合充能 +1）")
print(player_name, "VS", enemy_name)

turn = 1

# TODO(1) 雙方都活著才繼續
while ____ > 0 and ____ > 0:
    print("\n" + "=" * 36)
    print("第", turn, "回合")

    # TODO(2) 玩家回合開始：能量自動 +1
    player_energy = player_energy + ____
    print("[玩家回合開始] 你獲得 1 點能量！目前能量：", player_energy)

    print("你的HP:", player_hp, "| 對手HP:", enemy_hp)
    print("1)", move1_name, "-", move1_dmg, "(耗能", move1_cost, ")")
    print("2)", move2_name, "-", move2_dmg, "(耗能", move2_cost, ")")
    print("3) 用傷藥 +", potion_heal, "(剩", potion, ")")

    choice = input("選 1/2/3：").strip()

    # TODO(3) 招式1：能量夠才可用
    if choice == "1":
        if player_energy >= ____:
            player_energy = player_energy - ____
            enemy_hp = enemy_hp - ____
            print("你用了", move1_name, "！")
        else:
            print("能量不足！（本回合沒攻擊）")

    # TODO(4) 招式2：能量夠才可用
    elif choice == "2":
        if player_energy >= ____:
            player_energy = player_energy - ____
            enemy_hp = enemy_hp - ____
            print("你用了", move2_name, "！")
        else:
            print("能量不足！（本回合沒攻擊）")

    elif choice == "3":
        if potion > 0:
            potion = potion - 1
            player_hp = player_hp + potion_heal
            print("你用了傷藥！")
        else:
            print("傷藥用完了，這回合沒動作。")

    else:
        print("輸入錯誤，這回合沒動作。")

    # TODO(5) 對手倒下就結束
    if enemy_hp <= ____:
        break

    # TODO(6) 對手回合開始：能量自動 +1
    enemy_energy = enemy_energy + ____
    print("[對手回合開始]", enemy_name, "獲得 1 點能量！目前能量：", enemy_energy)

    # TODO(7) 對手AI：先能不能放招式2，不行再看招式1
    if enemy_energy >= ____:
        enemy_energy = enemy_energy - ____
        player_hp = player_hp - ____
        print(enemy_name, "用了", enemy_move2_name, "！")

    elif enemy_energy >= ____:
        enemy_energy = enemy_energy - ____
        player_hp = player_hp - ____
        print(enemy_name, "用了", enemy_move1_name, "！")

    else:
        print(enemy_name, "能量不足，這回合什麼都做不了！")

    turn = turn + ____

print("\n=== 結果判定 ===")
print("你的HP:", player_hp, "| 對手HP:", enemy_hp)

# TODO(8) 勝負判定（全部填 0）
if enemy_hp <= ____ and player_hp <= ____:
    print("同歸於盡！平手！")
elif enemy_hp <= ____:
    print("你贏了！")
else:
    print("你輸了！")
