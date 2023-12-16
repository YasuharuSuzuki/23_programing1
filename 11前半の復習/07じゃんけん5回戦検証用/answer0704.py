VicA = 0
VicB = 0
SA = []
SB = []
for i in range(5):
  A,B = input().split()
  SA.append(A)
  SB.append(B)
  if(SA[i] == "G"):
        if(SB[i] == "P"):
          VicB += 1
        elif(SB[i] == "C"):
          VicA += 1
        else:
          break
  elif(SA[i] == "C"):
        if(SB[i] == "P"):
          VicA += 1
        elif(SB[i] == "G"):
          VicB += 1
        else:
          break
  else:
       if(SB[i] == "C"):
        VicB += 1
       elif(SB[i] == "G"):
          VicA += 1
       else:
        break
print(VicA,VicB)
