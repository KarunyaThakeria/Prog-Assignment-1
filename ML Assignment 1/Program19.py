#Write a python program that removes all punctuation from a given string.

import string

input_string=str(input("Enter a string:"))
punctuation_set = set(string.punctuation)
result_string = ""
for char in input_string:
    if char not in punctuation_set:
        result_string += char

print("String without punctuation:", result_string)