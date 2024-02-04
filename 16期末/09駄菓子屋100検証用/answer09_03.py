N,S,E=map(int,input().split())
D=list(map(int,input().split()))
K=D[S-1:E]
K=sum(K)
A=K//100
R=K%100
print(f"{A} {R}")