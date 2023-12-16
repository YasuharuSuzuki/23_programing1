ASAN=0
BSAN=0
AIKO=0
for COUNT in range(5):
  A,B=input().split()
  if A=="G" and B=="C" or A=="C" and B=="P" or A=="P" and B=="G" :
    ASAN=ASAN+1
  elif A==B:
    AIKO=AIKO+1
  else:
    BSAN=BSAN+1
print(f"{ASAN} {BSAN}")
