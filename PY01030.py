import math
n, k=map(int, input().split())
a=[]
for i in range(10**(k-1), 10**k):
    if math.gcd(n, i)==1: a.append(i)

for i in range(len(a)):
    print(a[i], end=" ")
    if (i+1)%10==0: print()