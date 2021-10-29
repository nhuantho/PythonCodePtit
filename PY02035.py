s=input()
k=int(input())
a=[]
if len(s)%2!=0:
    for i in range(0, len(s)-3, 2):
        a.append(int(s[i:i+2]))
    a.append(int(s[len(s)-3: len(s)-1]))
else: 
    for i in range(0, len(s)-2, 2):
        a.append(int(s[i:i+2]))
    a.append(int(s[len(s)-2: len(s)]))
arr=[]
for i in range(100): arr.append(1)
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]==a[j]: 
            arr[a[j]]+=1
            a[j]=0
check=False
a.sort()
for i in a: 
    if i!=0 and arr[i]>=k: 
        print(i, arr[i])
        check=True
if check==False: print("NOT FOUND")
