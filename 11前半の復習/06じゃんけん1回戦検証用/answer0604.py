janken_list = ["G","C","P"]
SA, SB = input().split()
if SA == SB :
   print("あいこ")
elif SA == janken_list[0]:
        if SB == janken_list[1]:
           print("Aさんの勝ち")
        else:
           print("Bさんの勝ち")

elif SA == janken_list[1]:
        if SB == janken_list[2]:
           print("Aさんの勝ち")
        else:
           print("Bさんの勝ち")

else:
        if SB == janken_list[0]:
           print("Aさんの勝ち")
        else:
           print("Bさんの勝ち")
