ys,ye = map(int,input().split())
ori = 0
for i in range(ys,ye+1):
  if i>=1896:
    if i in [1916,1940,1944,2020]:
      kaisai = 0
    elif i%4 == 0 or i in [2021]:
      kaisai = 1
    else:
      kaisai = 0
  else:
    kaisai = 0
  ori += kaisai
print(ori)
