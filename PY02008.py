from math import sqrt
def snt(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False
    return True

n, x=map(int, input().split())
a=[]
a.append(2)
i=3
while True:
    if(snt(i)==True):
        a.append(i)
    if(len(a)==n): break
    i+=2
print(x, end=" ")
a[0]=a[0]+x
print(a[0], end=" ")
for i in range(1, len(a)):
    a[i]=a[i]+a[i-1]
    print(a[i], end=" ")