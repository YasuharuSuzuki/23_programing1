Y1,Y2 = map(int,input().split())
orinpic = 0
for y in range(Y1,Y2+1):

  if y<1896:
    orinpic_year = 0
  elif y%4 == 0:
      if y in [1916,1940,1944,2020]:
        orinpic_year = 0
      else:
        orinpic_year = 1
  elif y in [2021]:
    orinpic_year = 1
  else:
    orinpic_year = 0
  orinpic += orinpic_year

print(orinpic)
