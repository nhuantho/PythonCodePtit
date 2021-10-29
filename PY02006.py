'''Cho hai dãy số A[] và B[] có cùng N phần tử. Dãy số A[] được gọi là phù hợp với dãy số B[] 
khi và chỉ khi tồn tại một phép sắp đặt lại các phần tử trong A[] và B[] sao cho phần tử thứ i của A[] 
nhỏ hơn hoặc bằng phần tử thứ i của mảng B[] (với tất cả vị trí trong dãy).
Hãy xác định hai dãy số A[] và B[] có phù hợp với nhau hay không?'''
t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    a.sort()
    b.sort()
    check=True
    for i in range(0, n):
        if(a[i]>b[i]):
            check=False
    if check==True: print("YES")
    else: print("NO")
    t=t-1