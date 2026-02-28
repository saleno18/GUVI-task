# 1.Guess the number
import random

a = random.randint(1, 10)   # computer number
b = 0                       # user guess
while b != a:
    b = int(input("Enter number (1-10): "))
    if b == a:
        print("Correct")
    else:
        print("Incorrect")

# 2.Word Scramble
import random

a = ['python', 'java', 'selenium']
b = random.choice(a)     # original word
c = ""   # even letters
d = ""   # odd letters
for i in range(len(b)):
    if i % 2 == 0:
        c = c + b[i]
    else:
        d = d + b[i]
e = d + c   # join in different order
print("Unscrabled word:", e)
f = ""
while f != b:
    f = input("Enter word: ")
    if f == b:
        print("Correct!")
    else:
        print("Wrong, try again")
