#Write a program in python that counts the frequency of each character in a string.

s=str(input("Enter a string:"))
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    print(i,":",s.count(i))