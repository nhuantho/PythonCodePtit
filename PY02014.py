import math
def prime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

pr=[]
for i in range(10000):
    if prime(i)==True: pr.append(i)

n=int(input())
a=[int(x) for x in input().split()]
ID=0
for i in a:
    I=0
    for j in range(len(pr)):
        if pr[j]>=i: 
            I=j
            break
    ID=max(ID, min(abs(i-pr[I]), abs(i-pr[I-1])))
print(ID)
    
