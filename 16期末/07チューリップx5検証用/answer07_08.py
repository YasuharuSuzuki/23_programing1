all_color = {'赤','白','黄','桃','紫'}
set1 = set(input().split())
if len(set1) == 1:
   print(f"全部{set1.pop()}！")
elif len(set1) == 5:
   print("キレイだなぁ〜")
else:
   print('{}が欲しいなぁ～'.format("と".join(list(all_color - set1))))
