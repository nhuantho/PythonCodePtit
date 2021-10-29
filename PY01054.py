t=int(input())
for i in range(t):
    s=input()
    P=1
    for i in s:
        if int(i)!=0: P*=int(i)
    print(P)