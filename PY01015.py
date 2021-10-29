'''Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.
Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.'''
t=int(input())
while t>0:
    s=input()
    check=True
    for i in range(1, len(s)):
        if(s[i]<s[i-1]):
            check=False
            break
    if check==True: print("YES")
    else: print("NO")
    t=t-1
