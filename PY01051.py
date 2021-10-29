t=int(input())
for i in range(t):
    s=input()
    Sum=0
    for i in s: Sum+=int(i)
    x=list(str(Sum))
    x.reverse()
    S=""
    for i in x: S+=i
    if Sum==int(S) and Sum>10: print("YES")
    else: print("NO")