all = {'赤','白','黄','紫',"桃"}
input_set1 = set(input().split())
if len(input_set1) == 1:
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 5:
    print('キレイだなぁ〜')
else:
    print('{}が欲しいなぁ～'.format("と".join(list(all - input_set1))))
