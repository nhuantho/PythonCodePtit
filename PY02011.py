n=int(input())
a=[int(x) for x in input().split()]
SMIN=100000
MIN=100000
X=[]
for i in range(len(a)):
    SUM=0
    for j in a:
        SUM+=abs(a[i]-j)
    X.append([SUM, i])
X.sort()
print(X[0][0], a[X[0][1]])