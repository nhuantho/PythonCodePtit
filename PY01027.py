x=input()
s=list(x)
s.reverse()
check=False
for i in range(len(s)):
    check=False
    if s[i]=='6': check=True
    elif s[i]=='8' and s[i+1]=='6': 
        check=True
        if i+1==len(s)-1: break
    elif s[i]=='8' and s[i+1]=='8' and s[i+2]=='6':
        check=True
        if i+2==len(s)-1: break
    if check==False: break
if check==False: print("NO")
else: print("YES")