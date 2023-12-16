A, B = input().split()
if A == B:
    result = "あいこ"
elif (A == "G" and B == "C") or (A == "C" and B == "P") or (A == "P" and B == "G"):
    result = "Aさんの勝ち"
else:
    result = "Bさんの勝ち"
print(result)
