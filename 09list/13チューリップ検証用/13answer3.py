colors = input("花壇に植えたチューリップの色を漢字で入力してください（例：赤白黄）: ")

if colors[0] == colors[1] == colors[2]:
    print(f'全部{colors[0]}！')

elif colors[0] != colors[1] != colors[2] != colors[0]:
    print('キレイだなぁ〜')

else:
    if colors.count('赤') == 0:
        print('赤が欲しいなぁ〜')
    if colors.count('白') == 0:
        print('白が欲しいなぁ〜')
    if colors.count('黄') == 0:
        print('黄が欲しいなぁ〜')
