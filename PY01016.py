t=int(input())
while t>0:
    s=input()
    for i in range(0, len(s)):
        if(s[i]=='0' or s[i]=='1' or s[i]=='2' or s[i]=='3' or s[i]=='4' or s[i]=='5' or s[i]=='6' or s[i]=='7' or s[i]=='8' or s[i]=='9'):
            print(s[i-1]*int(s[i]), end="")
    print()
    t=t-1