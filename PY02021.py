t=int(input())
for i in range(t):
    a, b, c=map(int, input().split())
    sa=[int(x) for x in input().split()]
    sb=[int(x) for x in input().split()]
    sc=[int(x) for x in input().split()]
    i, j, k=0, 0, 0
    check=False
    while i<a and j<b and k<c:
        if sa[i]==sb[j] and sa[i]==sc[k]: 
            print(sa[i], end=" ")
            check=True
            i+=1
            j+=1
            k+=1
        elif sa[i]<sb[j]: i+=1
        elif sb[j]<sc[k]: j+=1
        else: k+=1 
    if check==False: print("NO", end="")
    print()
