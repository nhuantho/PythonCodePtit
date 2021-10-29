s=input()
a=[]
if len(s)%2!=0:
    for i in range(0, len(s)-3, 2):
        a.append(int(s[i:i+2]))
    a.append(int(s[len(s)-3: len(s)-1]))
else: 
    for i in range(0, len(s)-2, 2):
        a.append(int(s[i:i+2]))
    a.append(int(s[len(s)-2: len(s)]))
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]==a[j]: a[j]=0
a.sort()
for i in a: 
    if i!=0: print(i, end=" ")
