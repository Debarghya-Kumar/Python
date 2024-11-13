'''list_=[35,12,69,55,75,14,73]
l_list=list(filter(lambda num:(num%7==0),list_))

print("the list is",l_list)'''
n=int(input("Enter a number"))
is_prime=lambda num:all(num%i !=0 for i in range (2,int(num**.5)+1))
if is_prime(n)==True:
    print(n,"is prime")
else:
    print(n,"is not prime")
