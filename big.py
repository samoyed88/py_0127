import random

# 比大小（High Card）— 填空練習版
# 規則：每回合玩家與電腦各抽 1~13 的數字，數字大的人得 1 分。


def draw_number():
    """
    TODO 1:
    回傳一個 1~13 的隨機整數（包含 1 和 13）。
    提示：random.randint(?, ?)
    """
    return random.randint(1, 13)


def compare(a, b):
    """
    TODO 2:
    比較 a 和 b 的大小，回傳結果字串："win" / "lose" / "tie"
    提示：
    - 如果 a > b -> "win"
    - 如果 a < b -> "lose"
    - 否則 -> "tie"
    """
    if a > b:
        return "win"
    elif a < b:
        return "lose"
    else:
        return "tie"


def main():
    print("=== 比大小遊戲（填空版）===")

    # TODO 3:
    # 讓玩家輸入回合數 rounds（例如 5），並轉成整數
    # 提示：int(input("..."))
    rounds = int(input("要玩幾回合？請輸入整數，例如 5：").strip())

    # TODO 4:
    # 建立計分變數（玩家分數、電腦分數），一開始都是 0
    player_score = 0
    computer_score = 0

    # TODO 5:
    # 用迴圈玩 rounds 回合
    # 提示：for i in range(rounds):
    for i in range(rounds):
        print(f"\n--- 第 {i+1} 回合 ---")

        # 玩家與電腦各抽一個數字
        player_num = draw_number()
        computer_num = draw_number()

        print(f"你抽到：{player_num}")
        print(f"電腦抽到：{computer_num}")

        result = compare(player_num, computer_num)

        # TODO 6:
        # 根據 result 更新分數
        # 提示：
        # - win  -> player_score += 1
        # - lose -> computer_score += 1
        if result == "win":
            player_score += 1
            print("本回合：你贏！(+1)")
        elif result == "lose":
            computer_score += 1
            print("本回合：你輸。電腦 +1")
        else:
            print("本回合：平手（不加分）")

        # 印出目前比分（這段不用改）
        print(f"目前比分：你 {player_score} : 電腦 {computer_score}")

    # TODO 7:
    # 回合結束後，宣布最後勝負（比總分）
    # 提示：用 if/elif/else 比較 player_score 和 computer_score
    print("\n=== 最終結果 ===")
    print(f"你 {player_score} : 電腦 {computer_score}")

    if player_score > computer_score:
        print("恭喜你獲勝！")
    elif player_score < computer_score:
        print("電腦獲勝，下次加油！")
    else:
        print("平手！")


def play_round_once():
    """
    單局比大小（玩家 vs 電腦）

    行為：玩家與電腦各抽一個 1~13 的數字，印出抽到的數字與結果，
    並回傳結果碼：1=玩家贏，0=平手，-1=玩家輸
    """
    player_num = draw_number()
    computer_num = draw_number()

    print(f"你抽到：{player_num}")
    print(f"電腦抽到：{computer_num}")

    result = compare(player_num, computer_num)
    if result == "win":
        print("本局：你贏！")
        return 1
    elif result == "lose":
        print("本局：你輸。")
        return -1
    else:
        print("本局：平手。")
        return 0


def play_with_bet(bet=None):
    """
    與 `db.py` 整合的外部呼叫介面。

    參數 `bet` 為相容性保留（遊戲本身不會使用該數值），
    回傳 -1/0/1 分別代表輸/平/贏，由呼叫端負責依據下注金額進行結算。
    """
    return play_round_once()


if __name__ == "__main__":
    main()
