############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    # helper function
    def deal(dic):
        '''Deal a card'''
        dic["hand"].append(cards[random.randint(0, len(cards) - 1)])

    def updateHand(dic):
        '''Update score card'''
        dic["score"]["total"]["sum"] = 0
        dic["score"]["altTotal"]["sum"] = 0
        for card in dic["hand"]:
            if card == 11:
                dic["score"]["total"]["sum"] += 1
                dic["score"]["altTotal"]["sum"] += 11
            else:
                dic["score"]["total"]["sum"] += card
                dic["score"]["altTotal"]["sum"] += card
        for key in dic["score"]:
            if dic["score"][key]["sum"] > 21:
                dic["score"][key]["bust"] = True

    def checkBust(dic):
        '''Check if player is busted'''
        if dic["score"]["total"]["bust"] == True and dic["score"]["altTotal"][
                "bust"] == True:
            return True

    def countWinner(player, computer):
        '''count card for winners'''
        output = [
            "Computer",
            max(computer["score"]["total"]["sum"],
                computer["score"]["altTotal"]["sum"])
        ]
        for total in player["score"]:
            if player["score"][total]["sum"] > output[1] <= 21:
                output[0] = "Player"
                output[1] = player["score"][total]["sum"]
        return output

    #set the score card
    playerScore = {
        "hand": [],
        "score": {
            "total": {
                "sum": 0,
                "bust": False,
            },
            "altTotal": {
                "sum": 0,
                "bust": False,
            },
        }
    }
    computerScore = {
        "hand": [],
        "score": {
            "total": {
                "sum": 0,
                "bust": False,
            },
            "altTotal": {
                "sum": 0,
                "bust": False,
            },
        }
    }

    deal(playerScore)
    deal(playerScore)
    deal(computerScore)
    deal(computerScore)
    updateHand(playerScore)
    updateHand(computerScore)

    gameOver = False

    while gameOver == False:
        print(f"Your cards are {playerScore['hand']}")
        print(f"The computer's first card is {computerScore['hand'][0]}")
        hit = input("Type 'y' to get another card, 'n' to pass \n").lower()
        if hit == 'y':
            deal(playerScore)
            updateHand(playerScore)
            if checkBust(playerScore) == True:
                gameOver = True
                print("You went over! ")
        else:
            print(f"Your cards are {playerScore['hand']}")
            print(f"Computer's hand: {computerScore['hand']}")
            winner = countWinner(playerScore, computerScore)
            print(f"The winner is {winner[0]} with a score of {winner[1]}")
            gameOver = True


blackjack()
