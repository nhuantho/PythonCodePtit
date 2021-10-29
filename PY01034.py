t=int(input())
for i in range(t):
    s=input()
    s=list(s)
    check=False
    i=len(s)-1
    while i>=1:
        if int(s[i])<int(s[i-1]):
            Max=int(s[i])
            idM=i
            for j in range(i, len(s)):
                if int(s[j])>Max and int(s[j])<int(s[i-1]):
                    Max=int(s[j])
                    idM=j
            s[idM], s[i-1]=s[i-1], s[idM]
            check=True
            break
        i-=1
    if check==False or int(s[0])==0: print(-1)
    else: 
        for i in s: print(i, end="")
        print()