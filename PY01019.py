t=int(input())
while t>0:
    s1=input()
    s2=s1
    s1=list(s1)
    s2=list(s2)
    s2.reverse()
    check=True
    check=True
    for i in range(1, len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1]))!=abs(ord(s2[i])-ord(s2[i-1])):
            check=False
    if check==False: print("NO")
    else: print("YES")
    t-=1