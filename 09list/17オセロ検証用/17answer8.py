オセロ盤の状況=[input() for _ in range(8)]
白の石=sum(列.count('W') for 列 in オセロ盤の状況)
黒の石=sum(列.count('B') for 列 in オセロ盤の状況)
if 白の石 > 黒の石:
  print("YOU WIN")
elif 白の石 < 黒の石:
  print("YOU LOST")
else:
  print("EVEN")

