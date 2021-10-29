t=int(input())
for i in range(t):
    n=int(input())
    a=list()
    for i in range(1001): a.append(0)
    for i in range(n):
        x=int(input())
        a[x]+=1
    MAX=0
    VTM=0
    for i in range(1001):
        if(a[i]>MAX):
            MAX=a[i]
            VTM=i
    print(VTM)