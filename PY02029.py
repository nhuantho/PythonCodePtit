n, m=map(int, input().split())
arr=[int(x) for x in input().split()]
a=[]
for i in arr:
    if i<=m:
        if i in a: continue
        else: a.append(i)
TS=[]
for i in a:
        dem=0
        for j in arr:
            if i==j: dem+=1
        TS.append([dem, i])
TS.sort()
M2=0
VTM2=0
M1=TS[len(TS)-1][0]
check=False
for i in range(len(TS)):
    if TS[i][0]>M2 and TS[i][0]<M1:
        M2=TS[i][0]
        VTM2=TS[i][1]
        check=True
if check==False: print("NONE")
else: print(VTM2)