t=int(input())
for i in range(t):
    s=input()
    if len(s)%2==0 or s[0]==s[1]: print("NO")
    else:
        check=True
        for i in range(2, len(s), 2):
            if s[i]!=s[i-2]: 
                check=False
                break
        if check==False: print("NO")
        else: print("YES")