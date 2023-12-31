# ここ↓にPythonコードを記述してください
c1,c2,c3,c4 = input().split()
if (c1 == c2 == c3 == c4):
  print("全部",c1,"!")
elif (c1 != "赤") and (c2 != "赤") and (c3 != "赤") and (c4 != "赤") and (c1 != "白") and (c2 != "白") and (c3 != "白") and (c4 != "白"):
  print("赤と白が欲しいなぁ〜")
elif (c1 != "赤") and (c2 != "赤") and (c3 != "赤") and (c4 != "赤") and (c1 != "黄") and (c2 != "黄") and (c3 != "黄") and (c4 != "黄"):
  print("赤と黄が欲しいなぁ〜")
elif (c1 != "赤") and (c2 != "赤") and (c3 != "赤") and (c4 != "赤") and (c1 != "紫") and (c2 != "紫") and (c3 != "紫") and (c4 != "紫"):
  print("赤と紫が欲しいなぁ〜")
elif (c1 != "白") and (c2 != "白") and (c3 != "白") and (c4 != "白") and (c1 != "黄") and (c2 != "黄") and (c3 != "黄") and (c4 != "黄"):
  print("白と黄が欲しいなぁ〜")
elif (c1 != "白") and (c2 != "白") and (c3 != "白") and (c4 != "白") and (c1 != "紫") and (c2 != "紫") and (c3 != "紫") and (c4 != "紫"):
  print("白と紫が欲しいなぁ〜")
elif (c1 != "黄") and (c2 != "黄") and (c3 != "黄") and (c4 != "黄") and (c1 != "紫") and (c2 != "紫") and (c3 != "紫") and (c4 != "紫"):
  print("黄と紫が欲しいなぁ〜")
elif (c1 != c2) and (c2 != c3) and (c3 != c4) and (c4 != c1):
  print("キレイだなぁ〜")
elif (c1,c2,c3,c4 != "赤"):
  print("赤が欲しいなぁ〜")
elif (c1,c2,c3,c4 != "白"):
  print("白が欲しいなぁ〜")
elif (c1,c2,c3,c4 != "黄"):
  print("黄が欲しいなぁ〜")
elif (c1,c2,c3,c4 != "紫"):
  print("紫が欲しいなぁ〜")