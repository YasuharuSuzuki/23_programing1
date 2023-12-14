C1=list(input().split())
aka=int(C1.count("赤"))
siro=int(C1.count("白"))
ki=int(C1.count("黄"))
if aka==3 or siro==3 or ki==3 :
  if aka==3:
    print("全部赤！")
  elif siro==3:
    print("全部白!")
  else :
    print("全部黄!")
elif aka==0 or siro==0 or ki==0:
  if aka==0:
    print("赤が欲しいなぁ～")
  elif siro==0:
    print("白が欲しいなぁ～")
  else:
    print("黄が欲しいなぁ～")
elif aka==siro==ki:
  print("キレイだなぁ～")
