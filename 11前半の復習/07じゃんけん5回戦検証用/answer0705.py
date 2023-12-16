win_count_A = 0
win_count_B = 0
for _ in range(5):
    A, B = input().split()
    if A == B:
        continue
    elif (A == "G" and B == "C") or (A == "C" and B == "P") or (A == "P" and B == "G"):
        win_count_A += 1
    else:
        win_count_B += 1
print(f"{win_count_A} {win_count_B}")
