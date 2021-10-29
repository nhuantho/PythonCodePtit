import math
def snt(n):
    if n<2: return 0
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0): 
            return 0
    return 1
n=[int(x) for x in input().split()]
a=[]
for i in range(0, n[0]):
    arr=[int(x) for x in input().split()]
    a.append(arr)

for i in range(0, n[0]):
    for j in range(0, n[1]):
        print(snt(a[i][j]), end=" ")
    print()
