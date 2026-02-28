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
c = b[-1] + b[1:-1] + b[0]     #scrambling using slicing
print("Unscramble:", c)
d = ""
while d != b:
    d = input("Enter word: ")
    if d == b:
        print("Correct!")
    else:
        print("Wrong, try again")