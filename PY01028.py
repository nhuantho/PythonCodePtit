'''Nhập xâu ký tự S có độ dài không quá 100. Một từ được định nghĩa là một dãy ký tự không có khoảng trống.  
Hãy tách xâu S thành các từ, mỗi từ in trên một dòng.'''
s=[str(x) for x in input().split()]
for i in range(0, len(s)):
    print(s[i])