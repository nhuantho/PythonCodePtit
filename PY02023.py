#cach1
t=int(input())
for i in range(0, t):
    n=int(input())
    a=[int(x) for x in input().split()]
    arr=[]
    for i in a:
        x=str(i)
        s=0
        for j in x:
            s+=int(j)
        arr.append(s)  
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i]>=arr[j]:
                if(arr[i]==arr[j]):
                    if(a[i]>a[j]):
                        t=arr[i]
                        arr[i]=arr[j]
                        arr[j]=t
                        x=a[i]
                        a[i]=a[j]
                        a[j]=x
                else:
                    t=arr[i]
                    arr[i]=arr[j]
                    arr[j]=t
                    x=a[i]
                    a[i]=a[j]
                    a[j]=x
    for i in a:
        print(i, end=" ")
    print()
#cach2
def Sum(n):
    s=0
    n=str(n)
    for i in n:
        s+=int(i)
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
                