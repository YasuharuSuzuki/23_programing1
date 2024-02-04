n,s,e=map(int,input().split())
a=input().split()
total=0
count=0

for i in range(s-1,e):
    a[i]=int(a[i])
    total+=a[i]

count=total/100
count=int(count)

if count*100<total:
    count+=1

otsuri=count*100-total

print(count, otsuri)
