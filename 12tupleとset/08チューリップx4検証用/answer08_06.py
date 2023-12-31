# ここ↓にPythonコードを記述してください
zen={"赤","白","黄","紫"}
C=set(input().split())
nai=list(zen - C)
kazu=len(C)
C=list(C)
if kazu==1:
  print(f"全部{C[0]}!")
elif kazu==3 :
  print(f"{nai[0]}が欲しいなぁ～")
elif kazu==2:
  print(f"{nai[0]}と{nai[1]}が欲しいなぁ～")
else:
  print("キレイだなぁ～")
