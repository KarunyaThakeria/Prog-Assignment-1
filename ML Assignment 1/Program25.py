#Write a program that copies the contents of one text file to another.

source_file = "SampleText.txt" 
destination_file = "destination.txt"

with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
        for line in source:
            destination.write(line)
    print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")