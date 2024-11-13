
s1=int(input("Enter  1st side of a triangle: "))
s2=int(input("Enter 2nd side of a triangle: "))
s3=int(input("Enter 3rd side of a triangle: "))
if s1==s2==s3:
    print("Equilateral triangle")
elif s1!=s2 and s1!=s3 and s2!=s3:
    print("Scalene triangle")
else:
    print("Other triangle")
            
          
