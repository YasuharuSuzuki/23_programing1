ys, ye=map(int,input().split())
count=0

for i in range(ys, ye+1):
    if i>=1896:
        if i%4==0:
          count+=1

        if i==1916 or i==1940 or i==1944 or i==2020:
           count-=1
        elif i==2021:
           count+=1
print(count)