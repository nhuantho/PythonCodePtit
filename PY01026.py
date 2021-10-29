t=int(input())
for i in range(t):
    s1=input()
    x1=list(s1)
    s2=input()
    x2=list(s2)
    x1.sort()
    x2.sort()
    print("Test " + str(i+1)+": ", end="")
    if len(x1)!=len(x2): print("NO")
    else:
        check=True
        for i in range(len(s1)):
            if x1[i]!=x2[i]:
                check=False
                break
        if check==False: print("NO")
        else: print("YES")