def maxmin(a, n, m):
    MAX=0
    MIN=100000
    for i in range(n):
        for j in range(m):
            if a[i][j]>MAX: MAX=a[i][j]
            if a[i][j]<MIN: MIN=a[i][j]
    return MAX-MIN

def xet(x, a, n, m):
    dem=0
    for i in range(n):
        for j in range(m):
            if a[i][j]==x: 
                dem+=1
    return dem

n, m=map(int, input().split())
a=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    a.append(arr)
x=maxmin(a, n, m)
if xet(x, a, n, m)==0: print("NOT FOUND")
else:
    print(x)
    for i in range(n):
        for j in range(m):
            if a[i][j]==x:
                s="Vi tri ["+str(i)+']'+'['+str(j)+']'
                print(s)