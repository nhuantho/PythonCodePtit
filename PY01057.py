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
        if snt(i)==True and snt(int(s[i]))!=True:    
            check=False
            break
        if snt(i)!=True and snt(int(s[i]))==True:
            check=False
            break
    if check==True: print("YES")
    else: print("NO")