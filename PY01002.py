'''Cho một phép toán có dạng a + b = c với a,b,c chỉ là các số nguyên dương có một chữ số.
Hãy kiểm tra xem phép toán đó có đúng hay không.'''
s=input()
x=[]
for i in range(0, len(s)):
    if(s[i]!='+' and s[i]!='=' and s[i]!=' '):
        x.append(int(s[i]))
if (x[0]+x[1])==x[2]: print("YES")
else: print("NO")