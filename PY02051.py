n=int(input())
a=[]
for i in range(n):
    arr=[int(x) for x in input().split()]
    a.append(arr)
if n==2: print(a[0][1]//2, a[0][1]-a[0][1]//2)
else:
    a1=(a[0][1]+(a[0][2]-a[1][2]))//2
    print(a1, end=" ")
    for i in a[0]:
        if i!=0:
            print(i-a1, end=" ")