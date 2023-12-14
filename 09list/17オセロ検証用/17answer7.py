# オセロ盤の状況を受け取る
board = [input() for _ in range(8)]

# 白と黒の石の数をカウント
white_count = sum(row.count('W') for row in board)
black_count = sum(row.count('B') for row in board)

# 勝敗を判定して出力
if white_count > black_count:
    print("YOU WIN")
elif white_count < black_count:
    print("YOU LOST")
else:
    print("EVEN")

