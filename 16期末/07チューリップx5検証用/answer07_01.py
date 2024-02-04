all_color=["赤", "白", "黄", "桃", "紫"]
c = input().split()

if c[0]==c[1]==c[2]==c[3]==c[4]:
    print(f"全部{c[0]}!")
elif c[0]!=c[1]!=c[2]!=c[3]!=c[4]!=c[0] and c[0]!=c[2] and c[1]!=c[3] and c[3]!=c[0]:
    print("キレイだなぁ～")
else:
    none_color = set(all_color)-set(c)
    none_color=list(none_color)
    if len(none_color)==1:
        print(f"{none_color[0]}が欲しいなぁ～")
    elif len(none_color)==2:
        print(f"{none_color[0]}と{none_color[1]}が欲しいなぁ～")
    elif len(none_color)==3:
        print(f"{none_color[0]}と{none_color[1]}と{none_color[2]}が欲しいなぁ～")
