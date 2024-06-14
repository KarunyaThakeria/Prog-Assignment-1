#Write a python program that takes a list of numbers and returns their sum.

n=int(input("Enter the number of terms for the list:"))
l=[]
for i in range(n):
    e=int(input("Enter the element:"))
    l.append(e)

s=0
for i in l:
    s=s+i
print("Sum:",s)