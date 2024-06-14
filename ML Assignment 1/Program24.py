#Write a program that acts as a simple calculator. 
# It should take two numbers and an operator (+, -, *, /) as input and print the result.

n1=float(input("Enter the first number:"))
n2=float(input("Enter the second number:"))
op=str(input("Enter an operator(+,-,*,/):"))

if op=="+":
    print(n1,"+",n2,"=",n1+n2)
elif op=="-":
    print(n1,"-",n2,"=",n1-n2)
elif op=="*":
    print(n1,"*",n2,"=",n1*n2)
elif op=="/":
    if n2==0:
        print("n2 can not be 0.")
    else:
        print(n1,"/",n2,"=",n1/n2)
else:
    print("Invalid Input.")