n=int(input())
a=[]
for i in range(n):  
    s=input()
    arr=list(s)
    a.append(arr)
Sum=0
for i in range(n):
    dem1=0
    dem2=0
    for j in range(n):
        if ord(a[i][j])==ord('C'):
            dem1+=1
        if ord(a[j][i])==ord('C'):
            dem2+=1
    if dem1>=2:
        Sum=Sum+(dem1*(dem1-1)//2)
        Sum=Sum+(dem2*(dem2-1)//2)
print(Sum)