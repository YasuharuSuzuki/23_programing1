w_count = 0
b_count = 0
n_count = 0

for i in range(8):
    S_i = [s for s in input()]
    for j in range(8):
        if S_i[j] == "W":
            w_count += 1
        elif S_i[j] == "B":
            b_count += 1
        elif S_i[j] == "_":
            n_count = 0

if w_count == b_count:
    print("EVEN")
elif w_count > b_count:
    print("YOU WIN")
elif w_count < b_count:
    print("YOU LOST")