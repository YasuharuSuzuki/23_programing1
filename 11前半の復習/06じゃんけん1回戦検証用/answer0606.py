SA,SB = input().split()
if(SA == "G"):
    if(SB == "P"):
      print("Ｂさんの勝ち")
    elif(SB == "G"):
      print("あいこ")
    else:
      print("Ａさんの勝ち")
elif(SA == "C"):
    if(SB == "P"):
      print("Ａさんの勝ち")
    elif(SB == "G"):
      print("Ｂさんの勝ち")
    else:
      print("あいこ")
else:
    if(SB == "P"):
      print("あいこ")
    elif(SB == "G"):
      print("Ａさんの勝ち")
    else:
      print("Ｂさんの勝ち")

