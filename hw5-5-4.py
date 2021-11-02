# Author: CMOB 11/2/2021

word_1 = str(input("Please enter the first word. "))
word_2 = str(input("Please enter the second word. "))
word_3 = str(input("Please enter the thrid word. "))

a = str.capitalize(word_1)
b = str.capitalize(word_2)
c = str.capitalize(word_3)

if a > b and a > c:
    if b > c:
        print(word_1, word_2, word_3)
elif a > b and a < c:
    if b < c:
        print(word_1, word_3, word_2)
elif a < b and a < c:
    if b > c:
        print(word_2, word_3, word_1)
elif a < b and a > c:
    if b > c:
        print(word_2, word_1, word_3)
elif a < b and a < c:
    if b < c:
        print(word_3, word_2, word_1)
elif a > b and a < c:
    if b < c:
        print(word_3, word_1, word_2)
