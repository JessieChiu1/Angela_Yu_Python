#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

# setup
chosen_word = word_list[random.randint(0,2)].lower()
displayWord = []
life = 6
gameOver = False

for char in range(0,len(chosen_word)):
  displayWord.append("_")

# game play loop
while gameOver == False:
  print(' '.join(displayWord))
  guess = input("Pick a letter! \n")
  if chosen_word.find(guess) > -1:
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
          displayWord[i] = guess
    if chosen_word == ''.join(displayWord):
      gameOver = True
      print("You win!")
  else:
    life -= 1
    if life == 0:
      gameOver = True
      print("You lose")
    else:
      print(f"You have {life} life left")