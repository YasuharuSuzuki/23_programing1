Ys, Ye = map(int,input().split())
s = 0
for y in range(Ys,Ye+1):
    s_per_year = 0
    if (Ys,Ye) in [1916,1940,1944,2020]:
      s = 0
    elif (Ys%400 == 0) and (Ye%400 == 0) and (1896<=Ys,Ye<=9999):
        s_per_year = 1
    elif (Ys%100 == 0) and (Ye%100 == 0):
        s_per_year = 1
    elif (Ys%4 == 0) and (Ye%4 == 0):
        s_per_year = 1
    s += s_per_year

print(s)
