C1,C2,C3,C4,C5 =input().split()
seed_set = set()
seed_set.add(C1)
seed_set.add(C2)
seed_set.add(C3)
seed_set.add(C4)
seed_set.add(C5)
flower_set=set(["赤","白","黄","桃","紫"])
color_set = flower_set - seed_set
C_list = list(color_set)
L =len(seed_set)
if L == 4:
  print(f"全部{C_list[0]}!")
elif L == 0:
  print("キレイだなぁ～")
elif L == 3:
  print(f"{C_list[0]}と{C_list[1]}と{C_list[2]}が欲しいなぁ～")
elif L == 2:
  print(f"{C_list[0]}と{C_list[1]}が欲しいなぁ～")
else :
  print(f"{C_list[0]}が欲しいなぁ～")