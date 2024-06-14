#Write a python program that checks if two strings are anagrams of each other.

str1 = str(input("Enter the first string:"))
str2 = str(input("Enter the second string:"))

check=False
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
if sorted(str1)==sorted(str2):
    check=True


if check==True:
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")