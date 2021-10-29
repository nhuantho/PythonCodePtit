import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=[int(x) for x in input().split()]
b=[]
for i in a: 
    if snt(i)==True: b.append(i)
b.sort()
m=0
for i in range(n):
    if snt(a[i])==True:
        a[i]=b[m]
        m+=1
    print(a[i], end=" ")
