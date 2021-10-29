t=int(input())
for i in range(t):
    n, p=map(int, input().split())
    s=0
    while n>0:
        s+=(n//p)
        n//=p
    print(s)
