colors = input()
color_set = set(colors)
if len(color_set) == 1:
    print(f"全部{colors[0]}！")
elif len(color_set) == 4:
    print("キレイだなぁ〜")
else:
    missing_colors = [color for color in ['赤', '白', '黄', '紫'] if color not in color_set]
    if missing_colors:
        print(f"{', '.join(missing_colors)}が欲しいなぁ〜")
    else:
        print("条件エラー!")