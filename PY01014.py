x, y, z=map(int, input().split())
check=False
b=y
while b<=z:
    if b>x:
        print(b-x, end=" ")
        check=True
    b+=y
if check==False: print(-1)