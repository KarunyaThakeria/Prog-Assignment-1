#Write a python program that counts the occurrences of a specific element in a list.

l=[1,1,2,2,2,2,3,2,12,4,3,4,9,56,7]
print("List:",l)
e=int(input("Enter the element:"))
print("Number of occurences of",e,"is",l.count(e))