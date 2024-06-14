#Write a program that takes a string input from the user and writes it to a text file.

s=str(input("Enter a string:"))
with open("output.txt","w") as file:
    file.write(s)

print("String has been written to output.txt")