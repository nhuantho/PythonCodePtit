s=input()
dh=int()
dt=int()
for i in range(0, len(s)):
    if(s[i]>='A' and s[i]<='Z'):
        dh=dh+1
    else: dt=dt+1
if(dh>dt): print(s.upper())
else: print(s.lower())