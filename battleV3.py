# ==========================================
# 寶可夢對戰（自動充能版 + 戰鬥場/備戰區）【挖空版】
# 只針對「新增：Active/Bench、補位、交換、while True 勝負」挖空
# ==========================================

# ------- 玩家：起始牌組（示範 1 Active + 2 Bench）-------
player_active_name = "沙奈朵"
player_active_hp = 30

# Bench 用「清單」存，每個元素是一隻寶可夢：[名字, HP]
player_bench = [
    [____TODO_1____, ____TODO_2____],
    [____TODO_3____, ____TODO_4____],
]

# ------- 對手：起始牌組（示範 1 Active + 2 Bench）-------
enemy_active_name = "快龍"
enemy_active_hp = 30

enemy_bench = [
    [____TODO_5____, ____TODO_6____],
    [____TODO_7____, ____TODO_8____],
]

# ------- 玩家招式（固定一套，簡化：不分是哪隻上場都用同一套）-------
move1_name = "魔法葉"
move1_dmg = 8
move1_cost = 1

move2_name = "精神強念"
move2_dmg = 12
move2_cost = 2

# ------- 對手招式（同樣固定一套，簡化）-------
enemy_move1_name = "龍爪"
enemy_move1_dmg = 7
enemy_move1_cost = 1

enemy_move2_name = "龍之波動"
enemy_move2_dmg = 11
enemy_move2_cost = 2

# ------- 能量（雙方都需要；每「位玩家」一份）-------
player_energy = 0
enemy_energy = 0

# ------- 道具 -------
potion = 2
potion_heal = 10

print("道館挑戰開始！（自動每回合充能 +1 + 戰鬥場/備戰區）")
print("你派出：", player_active_name, "｜對手派出：", enemy_active_name)

turn = 1

# =========================
# 主迴圈：改成 while True（因為勝負不只看兩個HP了）
# =========================
while ____TODO_9____:
    print("\n" + "=" * 44)
    print("第", turn, "回合")

    # -------------------------------------------------
    # 玩家回合開始：若 Active 已倒下，先嘗試從 Bench 補位
    # （這是新增重點）
    # -------------------------------------------------
    if player_active_hp <= 0:
        if len(player_bench) > 0:
            # 自動拉第一隻備戰上來（bench[0]）
            player_active_name = player_bench[____TODO_10____][____TODO_11____]
            player_active_hp = player_bench[____TODO_12____][____TODO_13____]
            player_bench.pop(0) # 移除被選中的備戰

            print("[你方補位] 你的戰鬥寶可夢倒下了！")
            print("改派上場：", player_active_name, "（HP", player_active_hp, "）")
        else:
            print("[你方落敗] 你的戰鬥寶可夢倒下，備戰區也空了。")
            print("你輸了！")
            ____TODO_16____  # 跳出遊戲

    # 玩家自動充能 +1（原本就有：這段不挖）
    player_energy = player_energy + 1
    print("[玩家回合開始] 你獲得 1 點能量！目前能量：", player_energy)

    # 顯示狀態：新增「Bench 顯示」
    print("你的Active：", player_active_name, "HP:", player_active_hp)
    print("你的Bench：", end=" ")
    if len(player_bench) == 0:
        print("（空）")
    else:
        for p in player_bench:
            # p[0] 是名字；p[1] 是HP（這是新增重點）
            print(p[____TODO_17____] + "(HP" + str(p[____TODO_18____]) + ")", end="  ")
        print()

    print("對手Active：", enemy_active_name, "HP:", enemy_active_hp)
    print("對手Bench數量：", len(enemy_bench))

    # 玩家選單（新增：4) 交換上場）
    print("\n你的行動：")
    print("1)", move1_name, "-", move1_dmg, "(耗能", move1_cost, ")")
    print("2)", move2_name, "-", move2_dmg, "(耗能", move2_cost, ")")
    print("3) 用傷藥 +", potion_heal, "(剩", potion, ")")
    print("4) 交換上場（把 Bench 的一隻換到 Active，本回合不攻擊）")

    choice = input("選 1/2/3/4：").strip()

    # ----------------------------
    # 玩家行動（招式/傷藥：原本就有，盡量不挖）
    # ----------------------------
    if choice == "1":
        if player_energy >= move1_cost:
            player_energy = player_energy - move1_cost
            enemy_active_hp = enemy_active_hp - move1_dmg
            print("你用了", move1_name, "！對手Active -", move1_dmg, "（你能量剩", player_energy, "）")
        else:
            print("能量不足！你放不出", move1_name, "。（本回合沒攻擊）")

    elif choice == "2":
        if player_energy >= move2_cost:
            player_energy = player_energy - move2_cost
            enemy_active_hp = enemy_active_hp - move2_dmg
            print("你用了", move2_name, "！對手Active -", move2_dmg, "（你能量剩", player_energy, "）")
        else:
            print("能量不足！你放不出", move2_name, "。（本回合沒攻擊）")

    elif choice == "3":
        if potion > 0:
            potion = potion - 1
            player_active_hp = player_active_hp + potion_heal
            print("你用了傷藥！Active +", potion_heal, "（剩", potion, "）")
        else:
            print("傷藥用完了，這回合沒動作。")

    # -------------------------------------------------
    # 新增重點：交換上場（swap）
    # -------------------------------------------------
    elif choice == "4":
        if len(player_bench) == 0:
            print("你的備戰區是空的，無法交換。（本回合沒動作）")
        else:
            print("要換哪一隻上場？")

            i = 1
            for p in player_bench:
                print(str(i) + ")", p[0], "HP", p[1])
                i = i + 1

            pick = input("輸入編號：").strip()

            #（示範版只接受 1 或 2）
            if pick == "1" or pick == "2":
                idx = int(pick) - 1

                if idx >= 0 and idx < len(player_bench):
                    # 交換：Active 放回 Bench，選中的 Bench 上場
                    old_name = player_active_name
                    old_hp = player_active_hp

                    player_active_name = player_bench[idx][____TODO_19____]
                    player_active_hp = player_bench[idx][____TODO_20____]

                    player_bench.pop(idx)           # 移除被選中的備戰
                    player_bench.append([old_name, old_hp])  # 舊Active回到備戰

                    print("你交換上場：", player_active_name, "（HP", player_active_hp, "）")
                    print("原本的", old_name, "回到備戰區。")
                else:
                    print("輸入超出範圍（本回合沒動作）。")
            else:
                print("輸入錯誤（本回合沒動作）。")

    else:
        print("輸入錯誤，這回合沒動作。")

    # -------------------------------------------------
    # 對手回合開始：若 Active 已倒下，先嘗試從 Bench 補位（新增重點）
    # -------------------------------------------------
    if enemy_active_hp <= 0:
        if len(enemy_bench) > 0:
            enemy_active_name = enemy_bench[____TODO_23____][____TODO_24____]
            enemy_active_hp = enemy_bench[____TODO_25____][____TODO_26____]
            enemy_bench.____TODO_27____(____TODO_28____)

            print("\n[對手補位] 對手的戰鬥寶可夢倒下了！")
            print("對手改派上場：", enemy_active_name, "（HP", enemy_active_hp, "）")
        else:
            print("\n[對手落敗] 對手戰鬥寶可夢倒下，備戰區也空了。")
            print("你贏了！")
            ____TODO_29____

    # 對手自動充能 +1（原本就有：不挖）
    enemy_energy = enemy_energy + 1
    print("\n[對手回合開始]", enemy_active_name, "獲得 1 點能量！對手能量：", enemy_energy)

    # 對手 AI（原本就有：不挖）
    if enemy_energy >= enemy_move2_cost:
        enemy_energy = enemy_energy - enemy_move2_cost
        player_active_hp = player_active_hp - enemy_move2_dmg
        print(enemy_active_name, "用了", enemy_move2_name, "！你的Active -", enemy_move2_dmg, "（對手能量剩", enemy_energy, "）")

    elif enemy_energy >= enemy_move1_cost:
        enemy_energy = enemy_energy - enemy_move1_cost
        player_active_hp = player_active_hp - enemy_move1_dmg
        print(enemy_active_name, "用了", enemy_move1_name, "！你的Active -", enemy_move1_dmg, "（對手能量剩", enemy_energy, "）")

    else:
        print(enemy_active_name, "能量不足，這回合沒有攻擊！")

    turn = turn + 1
