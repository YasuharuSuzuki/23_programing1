球根list = input().split()
球根 = set(球根list)
チューリップ = {"赤", "白","黄","紫"}
A = チューリップ - 球根
Alist = list(A)
if len(A) == 0 :
  print("キレイだなぁ～")
elif len(A) == 1 :
  print(f"{Alist[0]}が欲しいなぁ～")
elif len(A) == 2 :
  print(f"{Alist[0]}と{Alist[1]}が欲しいなぁ～")
else :
  print(f"全部{球根list[0]}！")
