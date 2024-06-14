#Write a python program that calculates the sum of the digits of a given number.

n=int(input("Enter a number:"))
sum = 0
for digit in str(n):  
    sum += int(digit)       

print("Sum of digits=",sum)
