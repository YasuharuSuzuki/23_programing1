# ここ↓にPythonコードを記述してください
a, b, c, d = input().split()
if a == b == c == d:
    print(f"全部{a}！")

elif a == "赤"  and b == "赤" and c == "白"and d =="白":
    print("黄と紫が欲しいなぁ～")
elif a == "赤" and b == "白" and c == "赤"and d =="白":
    print("黄と紫が欲しいなぁ～")
elif a == "赤" and b == "白" and c == "白"and d =="赤":
    print("黄と紫が欲しいなぁ～")

elif a == "白" and b == "白" and c == "赤"and d =="赤":
    print("黄と紫が欲しいなぁ～")
elif a == "白" and b == "赤" and c == "白"and d =="赤":
    print("黄と紫が欲しいなぁ～")
elif a == "白" and b == "赤" and c == "赤"and d =="白":
    print("黄と紫が欲しいなぁ～")

elif a == "黄" and b == "黄" and c == "紫"and d =="紫":
    print("赤と白が欲しいなぁ～")
elif a == "黄" and b == "紫" and c == "黄"and d =="紫":
    print("赤と白が欲しいなぁ～")
elif a == "黄" and b == "紫" and c == "紫"and d =="黄":
    print("赤と白が欲しいなぁ～")

elif a == "紫" and b == "紫" and c == "黄"and d =="黄":
    print("赤と白が欲しいなぁ～")
elif a == "紫" and b == "黄" and c == "紫"and d =="黄":
    print("赤と白が欲しいなぁ～")
elif a == "紫" and b == "黄" and c == "黄"and d =="紫":
    print("赤と白が欲しいなぁ～")

elif a == "赤" and b == "赤" and c == "黄"and d =="黄":
    print("白と紫が欲しいなぁ～")
elif a == "赤" and b == "黄" and c == "赤"and d =="黄":
    print("白と紫が欲しいなぁ～")
elif a == "赤" and b == "黄" and c == "黄"and d =="赤":
    print("白と紫が欲しいなぁ～")

elif a == "黄" and b == "黄" and c == "赤"and d =="赤":
    print("白と紫が欲しいなぁ～")
elif a == "黄" and b == "赤" and c == "黄"and d =="赤":
    print("白と紫が欲しいなぁ～")
elif a == "黄" and b == "赤" and c == "赤"and d =="黄":
    print("白と紫が欲しいなぁ～")

elif a == "赤" and b == "赤" and c == "紫"and d =="紫":
    print("白と黄が欲しいなぁ～")
elif a == "赤" and b == "紫" and c == "赤"and d =="紫":
    print("白と黄が欲しいなぁ～")
elif a == "赤" and b == "紫" and c == "紫"and d =="赤":
    print("白と黄が欲しいなぁ～")

elif a == "紫" and b == "紫" and c == "赤"and d =="赤":
    print("白と黄が欲しいなぁ～")
elif a == "紫" and b == "赤" and c == "紫"and d =="赤":
    print("白と黄が欲しいなぁ～")
elif a == "紫" and b == "赤" and c == "赤"and d =="紫":
    print("白と黄が欲しいなぁ～")

elif a == "白" and b == "白" and c == "黄"and d =="黄":
    print("赤と紫が欲しいなぁ～")
elif a == "白" and b == "黄" and c == "白"and d =="黄":
    print("赤と紫が欲しいなぁ～")
elif a == "白" and b == "黄" and c == "黄"and d =="白":
    print("赤と紫が欲しいなぁ～")

elif a == "黄" and b == "黄" and c == "白"and d =="白":
    print("赤と紫が欲しいなぁ～")
elif a == "黄" and b == "白" and c == "黄"and d =="白":
    print("赤と紫が欲しいなぁ～")
elif a == "黄" and b == "白" and c == "白"and d =="黄":
    print("赤と紫が欲しいなぁ～")

elif a == "白" and b == "白" and c == "紫"and d =="紫":
    print("赤と黄が欲しいなぁ～")
elif a == "白" and b == "紫" and c == "白"and d =="紫":
    print("赤と黄が欲しいなぁ～")
elif a == "白" and b == "紫" and c == "紫"and d =="白":
    print("赤と黄が欲しいなぁ～")

elif a == "紫" and b == "紫" and c == "白"and d =="白":
    print("赤と黄が欲しいなぁ～")
elif a == "紫" and b == "白" and c == "紫"and d =="白":
    print("赤と黄が欲しいなぁ～")
elif a == "紫" and b == "白" and c == "白"and d =="紫":
    print("赤と黄が欲しいなぁ～")

elif a != "白" and b != "白" and c != "白" and d != "白":
    print("白が欲しいなぁ～")
elif a != "赤" and b != "赤" and c != "赤" and d != "赤":
    print("赤が欲しいなぁ～")
elif a != "黄" and b != "黄" and c != "黄" and d != "黄":
    print("黄が欲しいなぁ～")
elif a != "紫" and b != "紫" and c != "紫" and d != "紫":
    print("紫が欲しいなぁ～")

else:
    print("キレイだなぁ～")