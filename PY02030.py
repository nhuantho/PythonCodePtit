import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
arr=[int(x) for x in input().split()]
a=[]
for i in arr:
    if i in a: continue
    else: a.append(i)
SUMn=sum(a)
SUM0=0
check=False
for i in range(len(a)):
    SUMn-=a[i]
    SUM0+=a[i]
    if snt(SUM0)==True and snt(SUMn)==True:
        print(i)
        check=True
        break
if check==False: print("NOT FOUND")