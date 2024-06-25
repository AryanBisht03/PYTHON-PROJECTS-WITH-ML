import random
from art import logo
print(logo)

number=random.randint(0,100)
easy=10
hard=5
print(f"The ans is {number}")
def easy_game(number):
  global easy
  while easy!=0:
    print(f"You have {easy} attempts remaining to guess the correct number")
    guess_the_number=int(input("Guess the number:"))
    if guess_the_number==number:
      print("You gessed it Right!")
      print("You Win!")
      exit()
    elif guess_the_number<number:
      print("Too Low")
    else:
      print("Too High")
    easy=easy-1
    
  if easy==0:
    print("You Loose")

def hard_game(number):
  global hard
  while hard!=0:
    print(f"You have {hard} attempts remaining to guess the correct number")
    guess_the_number=int(input("Guess the number:"))
    if guess_the_number==number:
      print("You gessed it Right!")
      print("You Win!")
      exit()
    elif guess_the_number<number:
      print("Too Low")
    else:
      print("Too High")
    hard=hard-1
  if hard==0:
    print("You Loose")

a="Welcome to the number guessing game"
b="I'am Thinking of a number between 1 and 100"
c=input("choose a difficulty level, Type 'easy' or 'hard':").lower()
print(a.title())
print(b.title())
print(c.title())
if c=="easy":
  easy_game(number)
else:
  hard_game(number)