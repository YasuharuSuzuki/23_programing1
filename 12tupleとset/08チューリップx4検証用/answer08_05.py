# ここ↓にPythonコードを記述してください
color_list = ["赤","白","黄","紫"]
Tarinai_color = color_list.copy()
C1,C2,C3,C4 = input().split()
Flower_color = {C1,C2,C3,C4}
Flower_color = list(Flower_color)
for i in range(len(Flower_color)):
    Tarinai_color.remove(Flower_color[i])
Tarinai_color = list(Tarinai_color)
if len(Flower_color) == 4:
    print("キレイだなぁ〜")
elif len(Flower_color) == 1:
    print(f"全部{Flower_color[0]}！")
elif len(Tarinai_color) == 1:
    print(f"{Tarinai_color[0]}が欲しいなぁ〜")
elif len(Tarinai_color) == 2:
    print(f"{Tarinai_color[0]}と{Tarinai_color[1]}が欲しいなぁ〜")
