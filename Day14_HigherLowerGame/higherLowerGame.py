from game_data import data
import random

def higherOrLower ():
  def pick():
    return random.choice(data)
  
  def pickWinner(a,b):
    if a["follower_count"] > b["follower_count"]:
      return "a"
    else:
      return "b"

  print("Welcome to higher or lower!\n")
  score = 0
  a = pick()
  gameOver = False

  while gameOver == False:
    b = pick()
    print(f"Compare A: {a['name']}, {a['description']} \n VS \n B: {b['name']}, {b['description']}")
    userPick = input("\nWho has more followers? 'A' or 'B'?").lower()
    winner = pickWinner(a,b)
    print(f"{a['name']} has {a['follower_count']} vs {b['name']} has {b['follower_count']} \n")
    
    if winner == userPick:
      score += 1
      a = b
      b = pick()
    else:
      gameOver = True
      print(f"You final score is {score} \n")
      
higherOrLower()