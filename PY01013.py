from math import gcd, sqrt
t=int(input())
while t>0:
    x, y=map(int, input().split())
    s=str(gcd(x, y))
    n=0
    for i in range(0, len(s)):
        n=n+ int(s[i])
    check=True
    if n<2: check=False
    else:
        for i in range(2, int(sqrt(n))+1):
            if(n%i==0):
                check=False
                break
    if check==True: print("YES")
    else: print("NO")
    t=t-1