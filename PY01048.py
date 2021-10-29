def  tlt(n):
    a, dem, i=0, 0, 1
    while i*(i+1)/2<n:
        a=float(n-i*(i+1)/2)/(i+1)
        if int(a)==a: dem+=1
        i+=1
    return dem

t=int(input())
for i in range(t):
    n=int(input())
    print(tlt(n))
                