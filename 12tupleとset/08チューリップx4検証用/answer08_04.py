# ここ↓にPythonコードを記述してください
iro = list(input().split())
color = ["赤","白","黄","紫"]
if iro.count("赤") == 4 or iro.count("白") == 4 or iro.count("黄") == 4 or iro.count("紫") == 4:
  print(f"全部{iro[0]}!")
elif iro.count("赤") == 0:
  if iro.count("白") == 0:
    print("赤と白が欲しいなぁ～")
  elif iro.count("黄") == 0:
    print("赤と黄が欲しいなぁ～")
  elif iro.count("紫") == 0:
    print("赤と紫が欲しいなぁ～")
  else:
    print("赤が欲しいなぁ～")
elif iro.count("白") == 0:
  if iro.count("黄") == 0:
    print("白と黄が欲しいなぁ～")
  elif iro.count("紫") == 0:
    print("白と紫が欲しいなぁ～")
  else:
    print("白が欲しいなぁ～")
elif iro.count("黄") == 0:
  if iro.count("紫") == 0:
    print("黄と紫が欲しいなぁ～")
  else:
    print("黄が欲しいなぁ～")
elif iro.count("紫") == 0:
  print("紫が欲しいなぁ～")
else:
  print("キレイだなぁ～")