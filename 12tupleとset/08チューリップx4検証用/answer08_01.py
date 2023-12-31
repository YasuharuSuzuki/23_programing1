tulip_colors = input().split()
unique_colors = set(tulip_colors)
if len(unique_colors) == 1:
    print(f"全部{tulip_colors[0]}！")
elif len(unique_colors) == 4:
    print("キレイだなぁ〜")
else:
    missing_colors = set(['赤', '白', '黄', '紫']) - unique_colors
    if len(missing_colors) == 1:
        print(f"{missing_colors.pop()}が欲しいなぁ〜")
    else:
        color1, color2 = missing_colors
        print(f"{color1}と{color2}が欲しいなぁ〜")
