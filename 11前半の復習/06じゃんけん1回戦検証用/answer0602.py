SA,SB = (input().split())

if SA == SB:
    print("あいこ")
elif (SA == "G" and SB == "C") or (SA == "C" and SB == "P") or (SA == "P" and SB == "G"):
    print("Aさんの勝ち")
else:
    print("Bさんの勝ち")
