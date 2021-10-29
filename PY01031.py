p=list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
t=int(input())
for i in range(t):
    x, y=map(int, input().split())
    s=""
    while x>0:
        k=x%y
        s=p[k]+s
        x//=y
    print(s)