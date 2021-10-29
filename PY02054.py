n, m=map(int, input().split())
a=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    a.append(arr)
if n>m:
    x=n-m
    for i in range(0, x*2, 2):
        for j in range(m): a[i][j]=-1

    for i in range(n):
        for j in range(m): 
            if a[i][j]!=-1:
                print(a[i][j], end=" ")
        print()
else:
    x=m-n
    for i in range(1, x*2, 2):
        for j in range(n): a[j][i]=-1
    for i in range(n):
        for j in range(m): 
            if a[i][j]!=-1:
                print(a[i][j], end=" ")
        print()