C,S,E = map(int,input().split())
D = list(map(int,input().split()))
su = sum(D[S-1:E])
hyaku = int(su)//100
otu = int(su)-hyaku*100
print(f"{hyaku} {otu}")