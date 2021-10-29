t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    dem=1
    check=False
    for i in range(0, n-1):
        if(a[i]==a[i+1]):
            dem+=1
        else:
            if dem%2==1: 
                print(a[i])
                check=True
            dem=1
    if check==False: print(a[n-1])
    t-=1