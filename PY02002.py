t=int(input())
while t>0:
    x, y=map(int, input().split())
    a=[]
    a.append(1)
    a.append(1)
    for i in range(2, y):
        a.append(a[i-1]+a[i-2])
    for i in range(x-1, y):
        print(a[i], end=" ")
    print()
    t=t-1