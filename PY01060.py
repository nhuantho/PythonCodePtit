t=int(input())
for i in range(t):
    s=input()
    S, P, check=0, 1, False
    for i in range(len(s)):
        if i%2==1: S+=int(s[i])
        if i%2==0 and int(s[i])!=0:
            P*=int(s[i])
            check=True
    if check==True: print(P, S)
    else: print(0, S)
