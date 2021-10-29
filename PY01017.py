t=int(input())
while t>0:
    a=input()
    dem=int(0)
    for i in range(0, len(a)-1):
        if(a[i]==a[i+1]):
            dem=dem+1
        else: 
            print(str(dem+1)+a[i], end="")
            dem=0
    print(str(dem+1)+a[len(a)-1])
    t=t-1