n, k=map(int, input().split())
a=""
for i in range(n):
    s=input()
    a+=(s+" ")
a=a.lower()
S=""
for i in a:
    if ord(i)>=ord('0') and ord(i)<=ord('9'): S+=i
    elif ord(i)>=ord('a') and ord(i)<=ord('z'): S+=i
    else: S+=' '
S=[str(x) for x in S.split()]
SET=set(S)
DEM=[]
TS=set()
for i in SET:
    DEM.append([S.count(i), i])
    TS.add(S.count(i))
TS=list(TS)
TS.sort(reverse=True)
DEM.sort()
for i in TS:
    if i>=k: 
        for j in range(len(DEM)):
            if i==DEM[j][0]:
                print(DEM[j][1], i)