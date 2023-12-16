A = 0
B = 0

for i in range(5):
    a, b = input().split()
    if a == b:
        pass
    elif a == "G" and b == "C": # ✊ vs ✌️
        A += 1
    elif a == "C" and b == "P": # ✌️ vs ✋
        A += 1
    elif a == "P" and b == "G": # ✋ vs ✊
        A += 1
    else:
        B += 1
print(A, B)
