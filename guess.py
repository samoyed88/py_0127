import random

"""
random.randint(a, b)：整數（含頭含尾）
random.randrange(start, stop, step=1)：像 range 的隨機版（不含 stop
random.random()：0~1 的小數
random.uniform(a, b)：指定範圍小數
random.choice(seq)：隨機選 1 個
random.choices(seq, k=...)：可重複抽 k 個（像轉蛋）
random.sample(seq, k=...)：不重複抽 k 個（像抽籤）
random.shuffle(list)：原地洗牌（直接改原本 list）

"""



def play_guessing_game():
    """
    Interactive guessing game wrapper for external callers.
    Returns 1 if player guesses correctly, -1 if they quit (not used),
    and the number of tries as second value.
    """
    answer = random.randint(1, 100)  # 隨機產生 1~100 的整數答案
    tries = 0                        # 記錄猜的次數

    print("猜數字遊戲開始！範圍 1~100")

    while True:
        s = input("請輸入你的猜測 (或輸入 q 離開): ").strip()

        if s.lower() == 'q':
            print("遊戲中止。")
            return -1, tries

        # 防呆：不是整數就重輸入
        if not s.isdigit():
            print("請輸入整數（例如 42）")
            continue

        guess = int(s)
        tries += 1

        # 防呆：超出範圍
        if guess < 1 or guess > 100:
            print("超出範圍！請輸入 1~100")
            continue

        # 判斷大小
        if guess < answer:
            print("太小了")
        elif guess > answer:
            print("太大了")
        else:
            print(f"恭喜猜中！答案是 {answer}，你猜了 {tries} 次。")
            return 1, tries


if __name__ == '__main__':
    play_guessing_game()
