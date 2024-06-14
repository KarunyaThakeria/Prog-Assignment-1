#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

print("Menu:\n1.C to F\n2.F to C")
m=int(input("Enter the number of menu item:"))

if m==1:
    c=float(input("Enter temperature in Celsius:"))
    f=((9/5)*c)+32
    print("Temperature in Fahrenheit:",f)
elif m==2:
    f=float(input("Enter temperature in Fahrenheit:"))
    c=((f-32)*5)/9
    print("Temperature in Celsius:",c)
else:
    print("Invalid Input.")