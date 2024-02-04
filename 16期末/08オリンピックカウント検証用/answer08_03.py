YS,YE=map(int,input().split())
R=(YE-YS)//4
if 1896 > YS:
  M=1896-YS+1
  M=M//4
  R=R-M+1
if 1916 <= YS :
  R=R-1
if 1940 <= YS:
  R=R-1
if 1944 <= YS:
  R=R-1
if YE==2020:
  R=R-1
print(R)