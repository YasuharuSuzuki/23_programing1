A,B=input().split()
if A=="G" and B=="C" or A=="C" and B=="P" or A=="P" and B=="G" :
  print("Aさんの勝ち")
elif A==B:
  print("あいこ")
else:
  print("Bさんの勝ち")

