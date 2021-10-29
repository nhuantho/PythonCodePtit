import math
def snt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n, m=map(int, input().split())
a=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    a.append(arr)
Max, check=0, False
for i in range(n):
    for j in range(m):
        if snt(a[i][j])==True:
            if(a[i][j]>Max): 
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