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
    if snt(len(s))==False: print("NO")
    else:
        demt=0
        demf=0
        for i in s:
            if snt(int(i))==True: demt+=1
            else: demf+=1
        if demt>demf: print("YES")
        else: print("NO")