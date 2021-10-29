import math

l, r=map(int, input().split())
a=[]
for i in range(l, r):
    for j in range(i+1, r+1):
        if math.gcd(i, j)==1: a.append([i, j])
arr=[]
for i in range(len(a)):
    for j in range(a[i][0]+1, r+1):
        if math.gcd(a[i][0], j)==1 and math.gcd(a[i][1], j)==1 and j>a[i][1]: 
            s='('+str(a[i][0])+', '+str(a[i][1])+', '+str(j)+')'
            print(s)