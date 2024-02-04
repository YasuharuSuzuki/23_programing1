球根list = input().split()
球根 = set(球根list)
チューリップ = {"赤", "白","黄","紫","桃"}
A = チューリップ - 球根

if len(A) == 0 :
  print("キレイだなぁ～")
elif len(A) == 1 :
  print(f"{A[0]}が欲しいなぁ～")
elif len(A) == 2 :
  print(f"{A[0]}と{A[1]}が欲しいなぁ～")
elif len(A) == 3 :
  print(f"{A[0]}と{A[1]}と{A[2]}が欲しいなぁ～")
else :
  print(f"全部{球根list[0]}！")