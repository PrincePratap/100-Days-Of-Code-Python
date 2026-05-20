# fruite = ["apple", "banana", "cherry"]
# for fruit in fruite:
#     print(fruit)

# studentsMarks={86, 90, 78, 92, 88}
# sum = sum(studentsMarks)
# print("Total marks:", sum)\

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symabols = ["@", "#", "$", "%", "&", "*", "!", "?"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = ""
print("Welcome to the password generator!")
length = int(input("how many characters do you want in your password? "))
psSymbols  = int(input("how many symbols do you want in your password? "))
psNumbers = int(input("how many numbers do you want in your password? "))

for String in range(1, length + 1):
    password += random.choice(letters)
for String in range(1, psSymbols + 1):
    password += random.choice(symabols)
for String in range(1, psNumbers + 1):
    password += random.choice(numbers)

print("Your password is: " + password)