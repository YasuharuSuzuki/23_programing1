N, S, E = map(int,input().split())
D = list(map(int,input().split()))
Dn=(sum(D[S-1:E]))
if Dn%100 == 0:
  A=Dn/100
else:
  A=Dn/100+1
##
A=int(A)
A1=A*100
R=A1-Dn
R=int(R)
print(f"{A} {R}")
