A_win_count = 0
B_win_count = 0

for i in range(5):
    SAi,SBi = (input().split())
    if (SAi == "G" and SBi == "C") or (SAi == "C" and SBi == "P") or (SAi == "P" and SBi == "G"):
        A_win_count += 1
    elif (SBi == "G" and SAi == "C") or (SBi == "C" and SAi == "P") or (SBi == "P" and SAi == "G"):
        B_win_count += 1

print(f"{A_win_count} {B_win_count}")
