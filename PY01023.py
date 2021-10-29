from math import sqrt
t=int(input())
while t>0:
    n=int(input())
    print(1, '*', end=' ')
    for i in range(2, int(sqrt(n))+1):
        dem=0
        while n%i==0:
            dem+=1
            n//=i
        if n==1 and dem!=0: print(str(i)+'^' +str(dem))
        elif dem !=0: print(str(i)+'^'+ str(dem), end=' * ')
    if(n!=1): print(str(n)+'^' +'1')  
    t-=1