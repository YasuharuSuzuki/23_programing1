SASB = input()
Aの勝ち=["G C","C P","P G"]
Bの勝ち=["C G","P C","G P"]
if SASB in Aの勝ち:
  print("Aさんの勝ち")
elif SASB in Bの勝ち:
  print("Bさんの勝ち")
else :
  print("あいこ")
