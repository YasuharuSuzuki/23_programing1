color = ["赤","白","黄"]
buyColor = (input().split())

if buyColor[0] == buyColor[1] == buyColor[2]:
    print(f"全部{buyColor[0]}!")
elif buyColor[0] != buyColor[1] and buyColor[1] != buyColor[2] and buyColor[2] != buyColor[0]:
    print("キレイだなぁ～")
else:
    noneColor = set(color) - set(buyColor)
    noneColor = "".join(noneColor)
    print(f"{noneColor}が欲しいなぁ～")