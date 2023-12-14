list = input().split()
if list[0] == list[1] == list[2] :
    print("全部"+list[0]+"！")
elif "赤" not in list :
    print("赤が欲しいなぁ～")
elif "白" not in list :
    print("白が欲しいなぁ～")
elif "黄" not in list :
    print("黄が欲しいなぁ～")
else :
    print("キレイだなぁ～")

