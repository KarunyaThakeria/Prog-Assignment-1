#Write a python program that generates the first n numbers in the Fibonacci sequence.

n=int(input("Enter the number of terms:"))
n1=0
n2=1
if n==1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(1,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)