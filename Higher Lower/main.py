import random
from replit import clear
from art import logo
from art import vs
from game_data import data


def The_function(data):
  """
  The function prints the values like name, description and country of the celebrity or a club. 
  """
  print(f'{data["name"]}, a {data["description"]},from {data["country"]} ')


def comparision_function(compari1,compari2):
  """
  The function compares the followers count between 2 entities.
  """
  answer=""
  if compari1["follower_count"]>compari2["follower_count"]:
    answer="A"
  elif compari1["follower_count"]<compari2["follower_count"]:
    answer="B"
  return answer


comparisionA=random.choice(data)
comparisionB=random.choice(data)
game=True
score=0
while game==True:
  print(logo)
  if comparisionA!=comparisionB:
    The_function(comparisionA)  
    print(vs)
    The_function(comparisionB)
    answer_option=input("Who has more followers? Type 'A' or 'B':")
    
    if answer_option==comparision_function(comparisionA,comparisionB):
      game=True
      score=score+1
      comparisionA=comparisionB
      comparisionB=random.choice(data)
      clear()
    else:
      game=False
      print("Wrong Answer")

    print(f"Your Score is {score}")
      
  
  else:
    print("Please run it again! May be a Server Issue")
  