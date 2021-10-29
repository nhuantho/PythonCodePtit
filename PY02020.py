n=int(input())
a=[float(x) for x in input().split()]
a.sort()
Min, Max=a[0], a[n-1]
Sum=float(0)
dem=0
for i in a:
    if i!=Min and i!=Max: 
        Sum+=i
        dem+=1
print(format(Sum/dem, ".2f"))