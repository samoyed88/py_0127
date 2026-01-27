# 猜拳（石頭/剪刀/布）遊戲
#
# 規則：玩家選擇 石頭/剪刀/布（r/s/p），電腦隨機出一手。勝負規則：
# - 石頭 (r) > 剪刀 (s)
# - 剪刀 (s) > 布 (p)
# - 布 (p) > 石頭 (r)
#
# 介面：提供 play_with_bet(bet=None) 作為外部呼叫點，回傳 -1/0/1
#       - 1 -> 玩家贏
#       - 0 -> 平手
#       - -1 -> 玩家輸
#
import random


def _choice_to_name(ch):
    """把字元轉成中文名稱"""
    return {'r': '石頭', 's': '剪刀', 'p': '布'}.get(ch, '?')


def _judge(player, computer):
    """判定勝負：回傳 1/0/-1"""
    if player == computer:
        return 0
    # 贏的情況
    wins = {
        'r': 's',  # 石頭勝剪刀
        's': 'p',  # 剪刀勝布
        'p': 'r',  # 布勝石頭
    }
    if wins.get(player) == computer:
        return 1
    return -1


def play_round_interactive():
    """
    一局互動式猜拳：要求使用者輸入 r/s/p，並顯示結果。
    回傳 1/0/-1 表示勝/平/敗。
    """
    while True:
        s = input("請出拳（r=石頭, s=剪刀, p=布，或 q 離開）: ").strip().lower()
        if s == 'q':
            print('遊戲中止')
            return -1
        if s not in ('r', 's', 'p'):
            print('輸入不合法，請輸入 r/s/p')
            continue
        player = s
        computer = random.choice(['r', 's', 'p'])
        print(f"你: {_choice_to_name(player)}  vs 電腦: {_choice_to_name(computer)}")
        res = _judge(player, computer)
        if res == 1:
            print('你贏了！')
        elif res == -1:
            print('你輸了。')
        else:
            print('平手。')
        return res


def play_with_bet(bet=None):
    """
    與 `db.py` 整合的呼叫介面：執行一局猜拳，回傳 -1/0/1。
    `bet` 參數僅為相容性保留（遊戲內部不使用）。
    """
    return play_round_interactive()


if __name__ == '__main__':
    play_round_interactive()
