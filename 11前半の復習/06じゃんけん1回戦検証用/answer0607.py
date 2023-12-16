c1, c2 = map(str,input().split())
if c1 == 'G' and c2 == 'C':
    print("Aさんの勝ち")
elif c1 == 'C' and c2 == 'P':
    print("Aさんの勝ち")
elif c1 == 'P' and c2 == 'G':
    print("Aさんの勝ち")

elif c1 == 'C' and c2 == 'G':
    print("Bさんの勝ち")
elif c1 == 'P' and c2 == 'C':
    print("Bさんの勝ち")
elif c1 == 'G' and c2 == 'P':
    print("Bさんの勝ち")

elif c1 == 'C' and c2 == 'C':
    print("あいこ")
elif c1 == 'P' and c2 == 'P':
    print("あいこ")
elif c1 == 'G' and c2 == 'G':
    print("あいこ")
