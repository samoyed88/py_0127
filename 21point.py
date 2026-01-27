import random
# random 模組：用來做「隨機」
# 這裡會用到 random.shuffle（洗牌）

# ----------------------------
# 牌堆與點數規則
# ----------------------------

def create_deck():
    """
    建立牌堆（52 張，不含鬼牌）。
    我們用「tuple(元組)」表示一張牌：(rank, suit)
    - rank: "A", "2"... "10", "J", "Q", "K"
    - suit: "♠", "♥", "♦", "♣"

    回傳 deck：
    - deck 是一個 list，裡面有 52 個 (rank, suit)
    """

    # 四種花色（黑桃、紅心、方塊、梅花）
    suits = ["♠", "♥", "♦", "♣"]

    # 13 種牌面
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # 用「列表生成式」一次做出 52 張牌
    # 讀法：對每個 suit，再對每個 rank，產生 (rank, suit)
    deck = [(r, s) for s in suits for r in ranks]

    # 洗牌：random.shuffle 會「直接打亂 deck 本身」（原地修改）
    random.shuffle(deck)

    return deck


def card_str(card):
    """
    把一張牌轉成好看的字串，方便印出來。
    card 是 (rank, suit)，例如 ("A", "♠")
    """
    r, s = card  # tuple 解包：r 是 rank，s 是 suit
    return f"{r}{s}"


def hand_str(hand, hide_first=False):
    """
    把一手牌 hand（list of cards）轉成一行文字。

    hide_first=True 用在莊家：第一張牌要蓋住不給玩家看。
    例如：?? 7♦
    """
    # 防呆：如果 hand 是空的，回傳空字串
    if not hand:
        return ""

    if hide_first:
        # 第一張用 "??" 代替，後面的牌正常顯示
        shown = ["??"] + [card_str(c) for c in hand[1:]]
        # " ".join(...)：把清單中的文字用空白串起來
        return " ".join(shown)

    # 玩家手牌全部顯示
    return " ".join(card_str(c) for c in hand)


def hand_value(hand):
    """
    計算手牌點數（A 可算 11 或 1），這是 21 點的核心規則。

    規則：
    - "2"~"10"：照數字加
    - "J","Q","K"：都算 10
    - "A"：先當 11 加進去，如果總和爆掉（>21），再把某些 A 改成 1
      （改法：每把一張 A 從 11 改成 1，就等於總分 -10）
    """

    value = 0   # 目前總點數
    aces = 0    # 計算手上有幾張 A（等等可能要從 11 改成 1）

    # 逐張牌累加點數
    for rank, _suit in hand:
        # face cards：J/Q/K 都算 10
        if rank in ["J", "Q", "K"]:
            value += 10

        # A：先當 11
        elif rank == "A":
            value += 11
            aces += 1

        # 其他：就是數字牌 "2"~"10"
        else:
            value += int(rank)

    # 如果爆牌，而且手上還有 A
    # 就把 A 從 11 改成 1（總分 -10），直到不爆或沒有 A 可改
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value


def draw(deck, hand):
    """
    從牌堆 deck 抽一張牌加入 hand。

    deck 是 list（牌堆），我們用 deck.pop() 抽走「最後一張」：
    - pop() 會把那張牌「從 deck 移除」，並回傳那張牌
    - hand.append(...) 把抽到的牌放進手牌
    """
    hand.append(deck.pop())


# ----------------------------
# 一局遊戲流程
# ----------------------------

def play_round():
    """
    玩一局 21 點（玩家 vs 莊家）。
    一局結束會 return（回到 main 的重玩迴圈）。
    """

    # 建立牌堆並洗牌
    deck = create_deck()

    # 玩家與莊家的手牌（一開始都是空清單）
    player = []
    dealer = []

    # 初始發牌：玩家 2 張、莊家 2 張
    # 常見順序：玩家1、莊家1、玩家2、莊家2
    draw(deck, player)
    draw(deck, dealer)
    draw(deck, player)
    draw(deck, dealer)

    # 顯示初始狀態：
    # 莊家第一張要蓋牌（hide_first=True）
    print("\n=== 新的一局開始 ===")
    print(f"莊家手牌: {hand_str(dealer, hide_first=True)}")
    print(f"你的手牌: {hand_str(player)}  (點數: {hand_value(player)})")

    # ----------------------------
    # 玩家回合：要牌(hit) 或 停牌(stand)
    # ----------------------------
    while True:
        # 先計算玩家目前點數
        p_val = hand_value(player)

        # 如果玩家點數 > 21 就爆牌，這局直接輸
        if p_val > 21:
            print(f"你爆牌了（{p_val}）！你輸了。")
            return -1  # player bust -> lose

        # 讓玩家選擇：h 要牌、s 停牌
        cmd = input("選擇：h=要牌, s=停牌 : ").strip().lower()

        if cmd == "h":
            # 玩家要牌：抽一張
            draw(deck, player)

            # player[-1] 是「最後抽到的那張牌」
            print(f"你抽到: {card_str(player[-1])}")
            print(f"你的手牌: {hand_str(player)}  (點數: {hand_value(player)})")

        elif cmd == "s":
            # 玩家停牌：結束玩家回合，輪到莊家
            break

        else:
            # 防呆：輸入不是 h 或 s
            print("輸入無效，請輸入 h 或 s。")

    # ----------------------------
    # 莊家回合：至少補到 17
    # 常見規則：莊家點數 < 17 必須要牌
    # ----------------------------
    print("\n--- 莊家回合 ---")
    print(f"莊家亮牌: {hand_str(dealer)}  (點數: {hand_value(dealer)})")

    # 只要莊家點數還沒到 17，就一直抽牌
    while hand_value(dealer) < 17:
        draw(deck, dealer)
        print(f"莊家抽到: {card_str(dealer[-1])}")
        print(f"莊家手牌: {hand_str(dealer)}  (點數: {hand_value(dealer)})")

    # 回合結束後再取一次最終點數（避免重算太多次）
    d_val = hand_value(dealer)
    p_val = hand_value(player)

    # 如果莊家爆牌，玩家直接贏
    if d_val > 21:
        print(f"莊家爆牌了（{d_val}）！你贏了。")
        return 1

    # ----------------------------
    # 比大小（都沒爆的情況）
    # ----------------------------
    print("\n--- 結果 ---")
    print(f"你的點數: {p_val}")
    print(f"莊家點數: {d_val}")

    if p_val > d_val:
        print("你贏了！")
        return 1
    elif p_val < d_val:
        print("你輸了。")
        return -1
    else:
        # push：平手
        print("平手（Push）！")
        return 0


# ----------------------------
# 主程式：可重玩
# ----------------------------

def main():
    """
    主程式：負責顯示開場文字、並讓玩家選擇要不要再玩一局。
    """

    print("21 點（Blackjack）文字遊戲")
    print("目標：點數越接近 21 越好，超過 21 就爆牌。")

    # 重玩迴圈
    while True:
        # 玩一局（play_round 自己會印出過程與結果），回傳 1/0/-1
        play_round()

        # 問是否再玩
        again = input("\n再玩一局？(y/n): ").strip().lower()
        if again != "y":
            print("遊戲結束。")
            break


# Python 慣例：只有「直接執行」這個檔案，才會從 main() 開始跑
# 如果這份檔案被別的程式 import，就不會自動開始遊戲
if __name__ == "__main__":
    main()


def play_with_bet(bet=0):
    """
    Wrapper for external callers.
    Runs one interactive round and returns an integer multiplier:
      1  => player wins (net +bet)
      0  => push (refund)
     -1  => player loses (net -bet)

    The `bet` parameter is accepted for API compatibility but this function
    does not itself change any balance; that is managed by the caller.
    """

    result = play_round()
    # play_round already returns -1/0/1 per outcome
    return result
