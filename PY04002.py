a=input().split()
d, r, c=int(a[0]), int(a[1]), a[2]
if d>0 and r>0:
    print((d+r)*2, d*r, c.title())
else:
    print("INVALID")
