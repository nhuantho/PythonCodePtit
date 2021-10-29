n=int(input())
a=[]
for i in range(n):
    s=input()
    Sum=0
    check=False
    for i in s:
        if ord(i)>=ord('0') and ord(i)<=ord('9'):
            Sum=Sum*10+int(i)
            check=True
        else:
            if check==True:
                a.append(Sum)
            Sum=0
            check=False
    if check==True: a.append(Sum)
a.sort()
for i in a: print(i)