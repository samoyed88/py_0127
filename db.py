"""
簡單的籌碼管理器與遊戲選單。

功能：
- 管理單一玩家的籌碼（存在記憶體）
- 提供 `get_balance`, `change_balance`, `place_bet` API
- 可以選擇整合的遊戲並下注（呼叫其他模組提供的 play_xxx 函式）

使用方法：
 直接執行 `python db.py` 會顯示文字選單。
 如果作為模組匯入，請使用 API 函式。

注意：目前只支援單一玩家（user id 為 'player'）。
"""

import importlib
import sys

# 內存中的簡單資料庫（以字典保存玩家籌碼）
_balances = {"player": 1000}  # 預設初始籌碼


def get_balance(user="player"):
    return _balances.get(user, 0)


def change_balance(user, delta):
    """增加或減少籌碼，回傳新的餘額。"""
    _balances[user] = _balances.get(user, 0) + delta
    return _balances[user]


def place_bet(user, amount):
    """嘗試下注：如果金額合法且有足夠籌碼，扣款並回 True，否則回 False。"""
    bal = get_balance(user)
    if amount <= 0:
        return False, bal
    if amount > bal:
        return False, bal
    change_balance(user, -amount)
    return True, get_balance(user)


def load_game_module(name):
    """動態載入遊戲模組，回傳模組物件或 None。"""
    try:
        return importlib.import_module(name)
    except Exception as e:
        print(f"載入模組 {name} 失敗：{e}")
        return None


def run_game_with_bet(module_name, play_func_name='play_with_bet'):
    """
    從指定模組呼叫 play_func_name(game) 並依回傳值調整籌碼。

    規格（約定）：被呼叫的函式應回傳 -1/0/1（輸/平/贏）或其他語意相近的值。
    本函式會依照回傳值計算淨利：win -> +bet, lose -> -bet, push -> 0。
    """
    user = 'player'
    bal = get_balance(user)
    print(f"目前籌碼：{bal}")

    try:
        bet = int(input("請輸入下注金額: ").strip())
    except ValueError:
        print("輸入錯誤。請輸入整數。")
        return

    ok, newbal = place_bet(user, bet)
    if not ok:
        print(f"下注失敗。當前籌碼：{get_balance(user)}")
        return

    mod = load_game_module(module_name)
    if mod is None:
        print("無法載入遊戲模組，退還下注。")
        change_balance(user, bet)
        return

    # 取得 play 函式
    play = getattr(mod, play_func_name, None)
    if play is None:
        print(f"模組 {module_name} 中沒有 {play_func_name}() 函式。退還下注。")
        change_balance(user, bet)
        return

    print("開始遊戲...")
    # 執行遊戲：play 應回傳 -1/0/1 或類似
    try:
        res = play(bet)
    except TypeError:
        # 有些 play 函式可能不接受參數
        res = play()
    except Exception as e:
        print(f"執行遊戲發生例外：{e}")
        print("退還下注。")
        change_balance(user, bet)
        return

    # 決定賠率：預設 1:1（贏返回下注，輸則損失下注）
    if res == 1:
        # player wins -> give back 2x bet (因為已扣除 bet)，實際淨利為 +bet
        change_balance(user, bet * 2)
        print(f"你贏了！獲得 {bet}。目前籌碼：{get_balance(user)}")
    elif res == 0:
        # push -> refund bet
        change_balance(user, bet)
        print(f"平手，退還下注。籌碼：{get_balance(user)}")
    else:
        # lose or other -> no refund
        print(f"你輸了。籌碼：{get_balance(user)}")


def interactive_menu():
    # 只顯示三個遊戲：21 點 / 比大小 / 猜拳
    games = [
        ("21 點", "21point"),
        ("比大小", "big"),
        ("猜拳", "rps"),
    ]

    while True:
        print("\n=== 娛樂城主選單 ===")
        print(f"目前籌碼：{get_balance('player')}")
        for i, (label, _) in enumerate(games, start=1):
            print(f"{i}. {label}")
        print("0. 離開")

        choice = input("請選擇遊戲: ").strip()
        if choice == '0':
            print("離開，掰掰！")
            break

        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(games):
                print("請輸入有效的選項編號")
                continue
        except ValueError:
            print("請輸入數字選項")
            continue

        _, module_name = games[idx]
        run_game_with_bet(module_name)


if __name__ == '__main__':
    interactive_menu()
