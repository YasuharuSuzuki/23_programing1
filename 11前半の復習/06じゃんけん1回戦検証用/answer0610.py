a, b = input().split()
if a == b:
    print("あいこ")
elif a == "G" and b == "C":
    print("Aさんの勝ち")
elif a == "C" and b == "P":
    print("Aさんの勝ち")
elif a == "P" and b == "G":
    print("Aさんの勝ち")
else:
    print("Bさんの勝ち")
