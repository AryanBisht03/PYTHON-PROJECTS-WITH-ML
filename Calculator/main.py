# Calculator
from art import logo
from replit import clear
print(logo)
def add(num1,num2):
  return num1+num2

def subtract(num1,num2):
  return num1-num2

def multiply(num1,num2):
  return num1*num2

def division(num1,num2):
  return num1/num2

def floor_division(num1,num2):
  return num1//num2

def exponential(num1,num2):
  return num1**num2


def calculator():
  operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division,
    "//":floor_division,
    "**":exponential
  }
  
  num1=float(input("Enter first number"))
  
  
  for i in operations:
    print(i)
  
  flag=True
  while flag:
    operation=input("Pick an operation from the above")
    calculation_function=operations[operation]
    num2=float(input("Enter next number"))
    answer=calculation_function(num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
    mark_down=input(f'Type "y" to continue with {answer},or type "n" to exit, or type "nn" to off the application').lower()
    if mark_down=="y":
      num1=answer
    elif mark_down=="nn":
      exit()
    else:
      flag=False
      clear()
      calculator()

calculator()