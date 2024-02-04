N,S,E = map(int,input().split())
D = list(map(int,input().split()))
goukei = 0
for i in range(S,E+1):
  goukei = D[i-1] + goukei

if(goukei%100 == 0):
  en = goukei // 100
else:
  en = goukei // 100 + 1

oturi = en*100 - goukei
print(en,oturi)