s=input()
dem=0
while len(s)>1:
    a=0
    for i in s:
        a+=(ord(i)-ord('0'))
    s=str(a)
    dem+=1
print(dem)