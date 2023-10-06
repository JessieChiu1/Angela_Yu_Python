import os

bidLeft = True

bid = {}

while bidLeft == True:
    name = input("What is your name?")
    price = input("What is the highest price you are willing to pay?")
    bid[name] = price
    bidderLeft = input("Are there any other bidders? Type 'Yes' or 'No'")
    os.system("cls")
    if bidderLeft == "No":
        bidLeft = False


print(bid)
highestBidder = ""
highestBidderPrice = 0
for person in bid:
  if int(bid[person]) > highestBidderPrice:
      highestBidder = person
      highestBidderPrice = int(bid[person])
print(f"The winner is {highestBidder} with a bid of ${highestBidderPrice}")