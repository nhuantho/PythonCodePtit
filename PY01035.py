s=input()
a=list(s)
a.reverse()
x=0
for i in range(0, len(a)):
    x=x+int(a[i])*2**i
x=oct(x)
print(x[2:])