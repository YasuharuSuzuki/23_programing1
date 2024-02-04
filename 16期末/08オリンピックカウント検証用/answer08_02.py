Syear,Fyear = map(int,input().split())
goukei = 0
year = Fyear
for i in  range(year > Syear):
  if(year%4 == 0)and(Syear>=1896):
    goukei = goukei + 1
    if year  in [1916,1940,1944,2020]:
      goukei = goukei - 1
      year = year - 1
    else:
      year = year - 1
  elif year in [2021]:
      goukei = goukei + 1
      year = year - 1
  else:
    year = year - 1
print(goukei)