t=int(input())
while t>0:
    s=input()
    if(s[0]==s[len(s)-2] and s[1]==s[len(s)-1]): print("YES")
    else: print("NO")
    t=t-1