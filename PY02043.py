t=int(input())
for i in range(t):
    s=input()
    n=input()
    x=len(n)
    n=int(n)
    dem, i=0, 0   
    while i<=len(s)-x:
        check=False
        if int(s[i:i+x])==n: 
            dem+=1
            check=True
        if check==True: i=i+x
        else: i+=1
    print(dem)
