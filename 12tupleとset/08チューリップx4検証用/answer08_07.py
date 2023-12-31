# ここ↓にPythonコードを記述してください
all_color = ["赤","白","黄","紫"]
C = input().split()

if C[0] == C[1] == C[2] ==C[3]:
    print(f"全部{C[0]}！")
elif C[0]!=C[1]!=C[2]!=C[3]!=C[0] and C[1]!=C[3] and C[0]!=C[2]:
    print("キレイだなぁ～")
else:
    none_color = set(all_color) - set(C)
    none_color = list(none_color)
    if len(none_color) == 1:
       print(f"{none_color[0]}が欲しいなぁ～")
    else:
       print(f"{none_color[0]}と{none_color[1]}が欲しいなぁ～")
