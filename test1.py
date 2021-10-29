def btk(i, n, a, c, k):
    for j in range(1, n+1):
        if(c[j]==False):
            a[i]=j
            c[j]=True
            if(i==n):
                for x in range(1, k+1):
                    print(a[x], end="")
                print(end=" ")
            else: btk(i+1, n, a, c, k)
            c[j]=False
p="ABCDEFGHIJKLMNOPQRSTVWXYZ"
s, k=map(str, input().split())
n, k=0, int(k)
for i in range(len(p)):
    if p[i]==s: n=i+1
a=list()
c=list()
List=list()
for i in range(0, n+1): 
    a.append(0)
    c.append(False)
btk(1, n, a, c, k)
print()