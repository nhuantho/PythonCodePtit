t=int(input())
while t>0:
    s=input()
    add=0
    x=""
    for i in s:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            add+=int(i)
        else: x+=i
    x=sorted(x)
    x.append(add)
    for i in x:
        print(i, end="")
    print()
    t-=1