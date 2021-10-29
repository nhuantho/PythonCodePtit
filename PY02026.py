n,m=map(int, input().split())
an=[int(x) for x in input().split()]
am=[int(x) for x in input().split()]
an.sort()
am.sort()
bn=[an[0]]
for i in range(1, n):
    if an[i]!=an[i-1]:bn.append(an[i])
bm=[am[0]]
for i in range(1, m):
    if am[i]!=am[i-1]:bm.append(am[i])
if len(bn)!=len(bm): print("NO")
else:
    check=True
    for i in range(len(bn)):
        if bn[i]!=bm[i]:
            check==False
            break
    if check==False: print("NO")
    else: print("YES")
