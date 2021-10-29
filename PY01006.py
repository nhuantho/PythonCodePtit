t=int(input())
while t>0:
    s=input()
    check=True
    for i in range(0, len(s)):
        if(s[i]!='4' and s[i]!='7'):
            check=False
            break
    if check==True:
        print("YES")
    else: print("NO")    
    t=t-1