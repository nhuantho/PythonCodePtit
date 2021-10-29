n=int(input())
a=[]
while True:
    s=[int(x) for x in input().split()]
    for i in s: a.append(i)
    if len(a)==n: break
b=[]
c=[]
for i in a: 
    if(i%2==0): b.append(i)
    else: c.append(i)
b.sort()
c.sort()
x=0
y=len(c)-1
for i in a:
    if i%2==0: 
        print(b[x], end=" ")
        x+=1
    else: 
        print(c[y], end=" ")
        y-=1
