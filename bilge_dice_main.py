"""
Bilge Dice

Rules at: http://www.jellyneo.net/?go=bilge_dice

https://shipwell.atlassian.net/browse/INT-560

- 2 human players start with 100 neopoints (NPs).
- Select the ante for the round - 10 or 50 NP.
- Randomly selected player goes first.
- Each player rolls 6 dice to start. 
	- Select die values to keep in your hand. You have to keep at least 1 die per roll. 
	- Reroll the remaining dice and select ones to keep until all 6 dice are in hand. 
- Your hand has to contain a 1 and 4 to qualify. 
	- Without the qualifiers your score is 0.
- If you qualify, the sum of the other 4 dice in your hand is your score (max 24).
- Player with the highest score wins.
- The ante is added to your NP total if you win, deducted if you lose, and nothing happens if you tie. 
- You can play again if neither player is bankrupt :D

"""

## Global Stuff ##

import random
import bilge_dice_display_funcs
from bilge_dice_Roll import Roll
from bilge_dice_Die import Die
from bilge_dice_Player import Player
from bilge_dice_Hand import Hand
from bilge_dice_Bank import Bank
import bilge_dice_game_funcs


## Gameplay ##

playing = True


# Print rules

print('\nWelcome to Bilge Dice!\n')
print('Rules: ')
print('~ 2 human players start with 100 neopoints (NPs). \n~ Select the ante for the round - 10 or 50 NP. \n~ Randomly selected player goes first. ')
print('~ Each player rolls 6 dice to start. \n~ Select die values to keep in your hand. You have to keep at least 1 die per roll.\n~ Reroll the remaining dice and select ones to keep until all 6 dice are in hand.')
print('~ Your hand has to contain a 1 and 4 to qualify. \n~ Without the qualifiers your score is 0. ')
print('~ If you qualify, the sum of the other 4 dice in your hand is your score (max 24). ')
print('~ Player with the highest score wins. \n~ The ante is added to your NP total if you win, deducted if you lose, and nothing happens if you tie. ')
print('~ You can play again if neither player is bankrupt :D \n')

# Initiate players, banks

player1 = Player(input(">> Player 1 - what's your name? "))
bank1 = Bank(player1)

while True:
	player2 = Player(input(">> Player 2 - what's your name? "))
	if player2.name == player1.name:
		print("You cannot use the same name as Player 1!")
	else:
		break
bank2 = Bank(player2)

# Show initial bank balances

print(bank1)
print(bank2)

while playing == True:

	# Prompt players to pick an ante for the round

	bilge_dice_game_funcs.pick_ante(bank1, bank2)

	# Reset players' hands

	hand1 = Hand(player1)
	hand2 = Hand(player2)

	# Randomly decide who goes first (bc the 2nd player has an advantage)

	first = random.randint(1,2)

	if first == 1:
		bilge_dice_game_funcs.player_turn(player1, hand1)
		bilge_dice_game_funcs.player_turn(player2, hand2)
	else:
		bilge_dice_game_funcs.player_turn(player2, hand2)
		bilge_dice_game_funcs.player_turn(player1, hand1)

	# Check qualifiers and calculate scores

	if hand1.qualified() == True and hand2.qualified() == True:
		print(player1.name + " scored " + str(hand1.score) + " and " + player2.name + " scored " + str(hand2.score) + "...")
		if hand1.score > hand2.score:
			bank1.win()
			bank2.lose()
			print(player1.name + " WINS! ")
		elif hand1.score < hand2.score:
			bank2.win()
			bank1.lose()
			print(player2.name + " WINS! ")
		else:
			bank1.tie()
			bank2.tie()
			print(player1.name + " and " + player2.name + " have TIED! ")

	elif hand1.qualified() == True and hand2.qualified() == False:
		bank1.win()
		bank2.lose()
		print(player1.name + " scored " + str(hand1.score) + " and " + player2.name + " didn't qualify... ")
		print(player1.name + " WINS! ")
	elif hand1.qualified() == False and hand2.qualified() == True:
		bank2.win()
		bank1.lose()
		print(player1.name + " didn't qualify and " + player2.name + " scored " + str(hand2.score) + "... ")
		print(player2.name + " WINS! ")
	elif hand1.qualified() == False and hand2.qualified() == False:
		bank1.tie()
		bank2.tie()
		print("Neither of you qualified :( Better luck next time! ")

	print(bank1)
	print(bank2)

	# Check if anyone is bankrupt - if so, game over

	if bank1.total <=0:
		print(player1.name + " is bankrupt...\nEverybody go home! ")
		playing = False
		break
	elif bank2.total <=0:
		print(player2.name + " is bankrupt...\nEverybody go home! ")
		playing = False
		break

	# Ask to play again

	while True:
		play = input(">> Would you like to play again? (y/n) ")
		if play.lower() == 'y':
			break
		elif play.lower() == 'n':
			playing = False
			print("Until next time, bye! ")
			break









