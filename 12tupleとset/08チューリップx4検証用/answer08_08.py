# ここ↓にPythonコードを記述してください
C1,C2,C3,C4 = (input().split())
if(C1 == C2 == C3 == C4):
  print("全部"+ C1 +"!")
elif(C1 != C2) and (C2 != C3) and (C3 != C4) and (C4 != C1)and(C1 != C3)and(C2 != C4):
  print("キレイだなぁ～")
elif(C1 != "赤")and(C2 != "赤")and(C3 != "赤")and(C4 != "赤")and(C1 != "白")and(C2 != "白")and(C3 != "白")and(C4 != "白"):
  print("赤と白が欲しいなぁ～")
elif(C1 != "赤")and(C2 != "赤")and(C3 != "赤")and(C4 != "赤")and(C1 != "黄")and(C2 != "黄")and(C3 != "黄")and(C4 != "黄"):
  print("赤と黄が欲しいなぁ～")
elif(C1 != "赤")and(C2 != "赤")and(C3 != "赤")and(C4 != "赤")and(C1 != "紫")and(C2 != "紫")and(C3 != "紫")and(C4 != "紫"):
  print("赤と紫が欲しいなぁ～")
elif(C1 != "白")and(C2 != "白")and(C3 != "白")and(C4 != "白")and(C1 != "黄")and(C2 != "黄")and(C3 != "黄")and(C4 != "黄"):
  print("白と黄が欲しいなぁ～")
elif(C1 != "白")and(C2 != "白")and(C3 != "白")and(C4 != "白")and(C1 != "紫")and(C2 != "紫")and(C3 != "紫")and(C4 != "紫"):
  print("白と紫が欲しいなぁ～")
elif(C1 != "黄")and(C2 != "黄")and(C3 != "黄")and(C4 != "黄")and(C1 != "紫")and(C2 != "紫")and(C3 != "紫")and(C4 != "紫"):
  print("黄と紫が欲しいなぁ～")
elif(C1 != "赤")and(C2 != "赤")and(C3 != "赤")and(C4 !="赤"):
  print("赤が欲しいなぁ～")
elif(C1 != "黄")and(C2 != "黄")and(C3 != "黄")and(C4 !="黄"):
  print("黄が欲しいなぁ～")
elif(C1 != "白")and(C2 != "白")and(C3 != "白")and(C4 !="白"):
  print("白が欲しいなぁ～")
else:
  print("紫が欲しいなぁ～")
