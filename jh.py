#Printing a series of numbers between m and n by taking a function named Odd_Even.
def Odd_Even(m,n):
    for i in range(m,n):
        if (i%2==0):
            print(i)
m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
Odd_Even(m,n)
