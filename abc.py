#Different patterns using the symbol "*" and numbers
#right_triangle
n=5
for i in range(1,n+1):
    print('*'*i)
    '|n'
#inverted right-triangle
n=5
for i in range(n,0,-1):
    print('*'*i)
    '|n'
#pyramid pattern
n=6
for i in range(1,n+1):
    print(''*(n-1)+'*'*(2*i-1))
    '|n'
#diamond pattern
n=5
for i in range(1,n+1):
    print(''*(n-1)+'*'*(2*i-1))
for i in range(n-1,0,-1):
    print(''*(n-1)+'*'*(2*i-1))
    '|n'
#number pyramid
n=5
for i in range(1,n+1):
    print(''*(n-i)+str(i)*i)
