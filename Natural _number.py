'''#WAP to print first n natural numbers using 'for' loop
n=int(input("Enter a number"))
for abc in range(1,n+1,4):
    print (abc)

#WAP to print first n natural numbers using 'while' loop
n=int (input("enter a number:"))
i=1
while (i<=n):
    print (i)
    i+=1

#WAP to add first nth natural numbers
n=int (input("Enter a range:"))
s=0
for i in range(i,n+1):
    s=s+i
print ("Sum will be: ",s)

#WAPP to print first nth natural numbers
n=int(input("Enter the range: "))
for i in range(1,n+1,1):
        print(i, end=" ")'''

#WAPP to calculate the factorial of a given number
n=int(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f*=i
print("The factorial is: ",f)
