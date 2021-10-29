'''Cho một dãy số A[] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. Tại mỗi bước, 
giá trị A[i] được thay thế bằng abs(A[i] – A[i+1]), riêng A[4] = abs(A[4]-A[0]).
Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.
Hãy đếm xem sau bao nhiêu bước thì dãy số A[] có cả 4 vị trí đều bằng nhau.'''

while True:
    arr=[int(x) for x in input().split()]
    if(arr[1]==0 and arr[2]==0 and arr[3]==0 and arr[0]==0): break
    i=int(0)
    if(arr[1]==arr[2] and arr[2]==arr[3] and arr[3]==arr[0]): print(0)
    else:
        while True:
            x=abs(arr[0])
            arr[0]=abs(arr[0]-arr[1])
            arr[1]=abs(arr[1]-arr[2])
            arr[2]=abs(arr[2]-arr[3])
            arr[3]=abs(arr[3]-x)
            i=i+1
            if(arr[1]==arr[2] and arr[2]==arr[3] and arr[3]==arr[0]): break  
            
        print(i)
