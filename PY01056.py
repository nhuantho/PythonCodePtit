import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
t=int(input())
for i in range(t):
    s=input()
    check=True
    for i in range(0, len(s)):
        if i%2==0 and int(s[i])%2!=0: 
            check=False
            break
        if i%2!=0 and int(s[i])%2==0:
            check=False
            break
    if check==False: print("NO")
    else:
        Sum=0
        for i in s: Sum+=int(i)
        if snt(Sum)==False: print("NO")
        else: print("YES")