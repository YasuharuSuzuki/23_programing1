iro = list(input().split())
if iro.count("赤") == 3:
  print("全部赤！")
elif iro.count("白") == 3:
  print("全部白！")
elif iro.count("黄") == 3:
  print("全部黄！")
elif iro.count("赤") == 0:
  print("赤が欲しいなぁ～")
elif iro.count("白") == 0:
  print("白が欲しいなぁ～")
elif iro.count("黄") == 0:
  print("黄が欲しいなぁ～")
else:
      print("きれいだなぁ～")
