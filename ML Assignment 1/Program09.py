#Write a python program that checks if a substring is present in a given string.

string=str(input("Enter the string:"))
sub_string=str(input("Enter the sub-string:"))

if sub_string in string:
    print("The substring is present in the given string.")
else:
    print("The substring is not present in the given string.")