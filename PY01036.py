t=int(input())
for i in range(t):
    n=int(input())
    Sum=float(0)
    if n%2==0:
        for i in range(2, n+1, 2):
            Sum+=1/i
    else:
        for i in range(1, n+1, 2):
            Sum+=1/i
    print(format(Sum, ".6f"))