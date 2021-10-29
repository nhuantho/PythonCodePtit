n=int(input())
a=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    a.append(arr)
k=int(input())
st, sd=0, 0
for i in range(n):
    for j in range(n): 
        if j<i: st+=a[i][j]
        if j>i: sd+=a[i][j]
if abs(st-sd)<=k: print("YES")
else: print("NO")
print(abs(st-sd))