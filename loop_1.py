'''s="Python is fun"
k=2
for i in range(len(s)):
    print(s[k:])
    k=k+2
    
s="Computer"
s=list(s)
while len(s):
    print(s.pop())
s="Serampore"
k=s.index("r")
print(k)'''
s="Deba 2024"
if s[4].isalpha():
    print(s)
elif s[5].isalpha():
    print(s[2:])
else:
    print(s[:-1:])
    
