n=int(input())
a=[int(x) for x in input().split()]
count=int(0)
for i in range(1, n):
    if(a[i]!=a[i-1]): count=count+1
print(count)