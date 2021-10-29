t=int(input())
while t>0:
    x, y, z=map(float, input().split())
    s=1
    i=0
    while s<=z:
        i+=1
        s=x*(1+y/100)**i
        
    print(i)
    t-=1