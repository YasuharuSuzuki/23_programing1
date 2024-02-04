all_color = {'赤','白','黄','紫','桃'}
input_set1 = set(input().split())
if len(input_set1) == 1:#要素を数える（要素が一つしかない場合）
    print(f'全部{input_set1.pop()}！')
elif len(input_set1) == 5:#要素が複数ある場合
    print('キレイだなぁ〜')
else:
    print('{}が欲しいなぁ〜'.format("と".join(list(all_color - input_set1))))
