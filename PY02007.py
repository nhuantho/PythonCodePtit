a=[]
while True:
    s=[int(x) for x in input().split()]
    for i in s:
        a.append(i)
    if len(a)==10: break
x=[]
for i in a:
    k=i%42
    check=True
    for j in x:
        if(j==k):
            check=False
            break
    if check==True: x.append(k)
print(len(x))
