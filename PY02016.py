'''Cho dãy số A[] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, 
yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.'''
t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    Max=int(0)
    dem=int(1)
    a.sort()
    value=int(0)
    for i in range(1, n):
        if(a[i]==a[i-1]):
            dem=dem+1
        else: 
            if dem>Max: 
                Max=dem
                value=a[i-1]
            dem=1
    if dem>Max: 
        Max=dem
        value=a[n-1]
    if(Max>n/2): print(value)
    else: print("NO")
    t=t-1