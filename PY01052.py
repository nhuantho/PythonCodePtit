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
    Sum=0
    for i in s:
        Sum+=int(i)
    if snt(Sum)==True: print("YES")
    else: print("NO")
    