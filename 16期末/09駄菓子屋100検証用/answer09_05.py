N, S, E = map(int,input().split())
D = list(map(int,input().split()))
all =sum(D[S-1:E])
if (all%100) == 0:
  A = all//100
  R = all%100
  print(A,R)
else:
  A = all//100
  R = all%100
  print(A+1,100-R)