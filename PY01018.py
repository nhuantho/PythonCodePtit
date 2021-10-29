p=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")  
while True:
    x=[str(x) for x in input().split()]
    if int(x[0])==0: break
    k=int(x[0])
    s=x[1]
    a=[]
    for i in s:
        for j in range(0, len(p)):
            if(ord(i)==ord(p[j])): 
                a.append(j)
                break
    res=[]
    for i in a:
        if i+k>len(p)-1:
            res.append(p[i+k-len(p)])
        else: res.append(p[i+k])
    res.reverse()
    for i in res:
        print(i, end="")
    print()