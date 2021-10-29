n=int(input())
a=[int(x) for x in input().split()]
b=[0]
for i in range(1, n+1):
    b.append(0)
for i in a:
    if i>0 and i<=n:
        b[i]=1
check=False
for i in range(1, n+1):
    if b[i]==0:
        check=True
        print(i)
        break
if check==False: print(n+1)