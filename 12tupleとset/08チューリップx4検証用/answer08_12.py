color_type = ["赤","白","黄","紫"]
color_str = input()
color = color_str.split()
color_count = [0]*len(color_type)
no_index = -1
for index in range(len(color_type)):
  color_count[index] = color_str.count(color_type[index])
  if color_count[index] == 0:
    no_index = index

if color_count[0] == color_count[1] == color_count[2] == color_count[3]:
  print("キレイだなぁ～")
elif color[0] == color[1] == color[2] == color[3]:
  print(f"全部{color[0]}！")
else:
  print(f"{color_type[no_index]}が欲しいなぁ～")
