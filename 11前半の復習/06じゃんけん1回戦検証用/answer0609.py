Sa,Sb=input().split()
if Sa==Sb:
  print("あいこ")
elif Sa=="G" and Sb=="C" :
  print("Aさんの勝ち")
elif Sa=="C" and Sb=="P" :
  print("Aさんの勝ち")
elif Sa=="P" and Sb=="G":
  print("Aさんの勝ち")
else :
  print("Bさんの勝ち")
