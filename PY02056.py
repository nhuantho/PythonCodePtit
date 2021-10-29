def snt(s):
    if len(s)==1: return False
    i=0
    check=True
    s1=""
    for i in s:s1=i+s1
    if int(s1)!=int(s): return False
    return True

n, m=map(int, input().split())
a=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    a.append(arr)
Max, check=0, False
for i in range(n):
    for j in range(m):
        if snt(str(a[i][j]))==True:
            if a[i][j]>Max: 
                Max=a[i][j]
                check=True
if check==False: print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j]==Max:
                s="Vi tri ["+str(i)+']'+'['+str(j)+']'
                print(s)
