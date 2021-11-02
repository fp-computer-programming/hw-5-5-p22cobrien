# Author: CMOB 11/2/2021

a_string = input("Enter a string please. ")
b_string = a_string[::-1]
if b_string == a_string:
    print(b_string)
    print(a_string)
else:
    print("Not a palindrome")
