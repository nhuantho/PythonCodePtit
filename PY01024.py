t=int(input())
while t>0:
    s=input()
    add=int(s[0])
    check=True
    for i in range(1, len(s)):
        add=add+int(s[i])
        if(abs(int(s[i])-int(s[i-1]))!=2):
            check=False
            break
    if check==True:
        if add%10!=0: check=False
    if check==True: print("YES")
    else: print("NO")
    t=t-1