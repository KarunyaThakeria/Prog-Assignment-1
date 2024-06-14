#Write a program that reads multiple lines of input from the user until they enter an empty line, 
#then prints all the lines.

print("Enter multiple lines of input. Press Enter on an empty line to finish.")
lines = []
while True:
    line = input("Enter a line (or press Enter to finish): ")
    if line == "":
        break
    lines.append(line)

print("\nAll lines entered:")
for line in lines:
    print(line)
