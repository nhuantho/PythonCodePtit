from math import sqrt
def snt(n):
    if(n<2): return False
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n=int(input())
a=[int(x) for x in input().split()]
s=[]
for i in range(0, n):
    dem=0
    if(snt(a[i])==True):
        dem+=1
        for j in range(i+1, n):
            if a[i]==a[j]: 
                dem+=1
                a[j]=0
    if(dem>0): print(a[i], dem)
