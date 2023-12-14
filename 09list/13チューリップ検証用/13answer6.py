color = ["赤","黄","白"]
C1, C2, C3 = input().split()
if C1 == C2 and C1 == C3 :
         print(f"全部{C1}!")

elif C1 == C2 :
         if C1 == color[0]:
            if C3 == color[1]:
               print(f"{color[2]}が欲しいなぁ〜")
            else:
               print(f"{color[1]}が欲しいなぁ〜")
         elif C1 == color[1]:
            if C3 == color[2]:
               print(f"{color[0]}が欲しいなぁ〜")
            else:
               print(f"{color[2]}が欲しいなぁ〜")
         elif C1 == color[2]:
            if C3 == color[0]:
               print(f"{color[1]}が欲しいなぁ〜")
            else:
               print(f"{color[0]}が欲しいなぁ〜")

elif C1 == C3 :
         if C1 == color[0]:
            if C2 == color[1]:
               print(f"{color[2]}が欲しいなぁ〜")
            else:
               print(f"{color[1]}が欲しいなぁ〜")
         elif C1 == color[1]:
            if C2 == color[2]:
               print(f"{color[0]}が欲しいなぁ〜")
            else:
               print(f"{color[2]}が欲しいなぁ〜")
         elif C1 == color[2]:
            if C2 == color[0]:
               print(f"{color[1]}が欲しいなぁ〜")
            else:
               print(f"{color[0]}が欲しいなぁ〜")

elif C2 == C3 :
         if C2 == color[0]:
            if C1 == color[1]:
               print(f"{color[2]}が欲しいなぁ〜")
            else:
               print(f"{color[1]}が欲しいなぁ〜")
         elif C2 == color[1]:
            if C1 == color[2]:
               print(f"{color[0]}が欲しいなぁ〜")
            else:
               print(f"{color[2]}が欲しいなぁ〜")
         elif C2 == color[2]:
            if C1 == color[0]:
               print(f"{color[1]}が欲しいなぁ〜")
            else:
               print(f"{color[0]}が欲しいなぁ〜")
else:
        print(f"キレイだなぁ〜")
