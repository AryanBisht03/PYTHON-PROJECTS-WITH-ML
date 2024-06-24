from replit import clear
from art import logo

def bidders(dict):
  highest_bid=0
  winner=""
  for bid in dict:
    bid_amount=dict[bid]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bid
  print(f"The winner is {winner} with a bid of ${highest_bid}")
print(logo)
dict={}
start=False
while not start:
  print("What is your name")
  name=input()
  bid=int(input("What is your bid: $"))
  dict[name]=bid
  should_start=input('Any other bidder wants to bid? Type "Yes" or "No"').lower()
  if should_start=="no":
    start=True
    bidders(dict)
  else:
    clear()
