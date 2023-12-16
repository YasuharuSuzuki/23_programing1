A,B = (input().split())
if A == B:
  print("あいこ")
elif A == "G" and B == "C" or A == "P" and B == "G" or A == "C" and B == "P":
  print("Aさんの勝ち")
elif A == "C" and B == "G" or A == "G" and B == "P" or A == "P" and B == "C":
  print("Bさんの勝ち")
