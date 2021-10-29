# Author: CMOB 10/29/2021

variable_1 = input("Enter a sentence. ")
length = len(variable_1)
length //= 2
print(variable_1[:length])
print(variable_1[length:])
