n,m=map(int, input().split())
an=[int(x) for x in input().split()]
am=[int(x) for x in input().split()]
bn=list()
bm=list()
for i in range(1001):
    bn.append(0)
    bm.append(0)
for i in an: bn[i]+=1
for i in am: bm[i]+=1
for i in range(1001): 
    if bn[i]!=0 and bm[i]!=0: print(i, end=" ")
print()
for i in range(1001):
    if bn[i]!=0 and bm[i]==0: print(i, end=" ")
print()
for i in range(1001):
    if bm[i]!=0 and bn[i]==0: print(i, end=" ")
