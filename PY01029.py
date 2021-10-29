import math
t=int(input())
for i in range(t):
    s=input()
    a=list(s)
    a.reverse()
    x=""
    for i in a: x+=i
    if math.gcd(int(s), int(x))==1: print("YES")
    else: print("NO")