t=int(input())
while t>0:
    s=input()
    a=list(s)
    i=len(a)-1
    s=""
    while i>0:
        if int(a[i])>=5:
            a[i-1]=str(int(a[i-1])+1)
            s='0'+s
        else: s='0'+s
        i-=1
    s=a[i]+s
    print(s)
    t-=1