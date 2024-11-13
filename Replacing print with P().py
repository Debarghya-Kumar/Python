#Replacing print function with P()
def P(x=None,y=None,z=None,k=None,l=None):
    if x==None:
        x=''
    if y==None:
        y='' 
    if z==None:
        z='' 
    if k==None:
        k='' 
    if l==None:
        l='' 
    print(x,y,z,k,l)
a=5
b=10
c=a+b
P(c)
    
