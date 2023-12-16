A_W = 0
B_W = 0
for i in range(5):
  A,B = input().split()
  if A == B:
      A_W += 0
  elif A == "G" and B == "C" or A == "P" and B == "G" or A == "C" and B == "P":
      A_W += 1
  elif A == "C" and B == "G" or A == "G" and B == "P" or A == "P" and B == "C":
      B_W += 1
print(A_W,B_W)