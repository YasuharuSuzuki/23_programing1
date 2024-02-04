Y = int(input())

eto_list = ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"]

eto_index = (Y - 2000 + 8) % 12
eto = eto_list[eto_index]

print(eto)
