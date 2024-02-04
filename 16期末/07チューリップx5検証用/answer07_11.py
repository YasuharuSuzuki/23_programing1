a, b, c, d, e = input().split()
if a == b == c == d == e:
    print(f"全部{a}！")
elif a != "白" and b != "白" and c != "白" and d != "白" and e != "白":
    print("白が欲しいなぁ～")
elif a != "赤" and b != "赤" and c != "赤" and d != "赤" and e != "赤":
    print("赤が欲しいなぁ～")
elif a != "黄" and b != "黄" and c != "黄" and d != "黄" and e != "黄":
    print("黄が欲しいなぁ～")
elif a != "紫" and b != "紫" and c != "紫" and d != "紫" and e != "紫":
    print("紫が欲しいなぁ～")
elif a != "桃" and b != "桃" and c != "桃" and d != "桃" and e != "桃":
    print("桃が欲しいなぁ～")
else:
    print("キレイだなぁ～")
