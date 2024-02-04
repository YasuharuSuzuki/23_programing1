color_type = ["赤","白","黄","桃","紫"]
colors_str = input()
color = colors_str.split()
color_count = [0]*len(color_type)
color_count = [1]*len(color_type)
color_count = [2]*len(color_type)
color_count = [3]*len(color_type)
color_count = [4]*len(color_type)
no_index = -1
for index in range(len(color_type)):
    color_count[index] = colors_str.count(color_type[index])
    if color_count[index] == 0:
        no_index = index

if color_count[0] == color_count[1] == color_count[2] == color_count[3] == color_count[4]:
    print("キレイだなぁ〜")
elif color[0] == color[1] == color[2]:
    print(f"全部{color[0]}！")
else:
    print(f"{color_type[no_index]}が欲しいなぁ〜")