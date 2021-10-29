s=input()
n=len(s)-1
a=""
i=0
while True:
    i+=1
    a=s[n]+a
    if n==0: break
    if i==3: 
        a=','+a
        i=0
    n-=1
print(a)
