siro=0
kuro=0
for i in range(8):
    S_i=input()
    for N in range(8):
        if S_i[N]=="W":
            siro+=1
        elif S_i[N]=="B":
            kuro+=1

if siro<kuro:
    print("YOU LOST")
elif kuro<siro:
    print("YOU WIN")
else:
    print("EVEN")
