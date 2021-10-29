def Sum(n):
    s=1
    n=str(n)
    for i in n:
        s*=int(i)
    return s

t=int(input())
for i in range(0, t):
    n=int(input())
    a=[int(x) for x in input().split()]
    arr=[]
    for i in a:
        arr.append([Sum(i), i])
    arr.sort()
    for i in range(0, n):
        print(arr[i][1], end=" ")
    print()