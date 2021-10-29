p=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
t=int(input())
for i in range(t):
    s=input()
    a=list(s[:len(s)//2])
    b=list(s[len(s)//2:])
    S1, S2=0, 0
    k=[]
    for i in range(len(a)):
        S1+=(ord(a[i])-ord('A'))
        S2+=(ord(b[i])-ord('A'))
        k.append(ord(a[i])-ord('A')+ord(b[i])-ord('A'))
    x=""
    for i in k:
        Sum=i+S1+S2
        x+=p[Sum%26]
    print(x)