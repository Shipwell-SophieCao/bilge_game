import bilge_dice_display_funcs
from bilge_dice_Roll import Roll
from bilge_dice_Die import Die
from bilge_dice_Player import Player
from bilge_dice_Hand import Hand
from bilge_dice_Bank import Bank

## Game Functions ##

def pick_ante(bank1, bank2):
	'''
	Ask players to pick an ante for the round. You can only bet 10 or 50, and no more than what you have in the bank. 
	'''
	while True:
		try:
			ante = int(input(">> Pick the ante for this round - 10 or 50 NP? "))
		except ValueError:
			print("Bet must be an integer value!")
		else: 
			if ante != 10 and ante != 50 and ante != 0:
				print("Sorry, you can only pick an ante of 10 or 50 NP.")
			elif ante == 0:
				print("Sorry, you can't bet 0 NP. :(")
			elif ante > bank1.total or ante > bank2.total:
				print("Sorry, you can bet a maximum of ", min(bank1.total, bank2.total), " NP.")
			else:
				bank1.ante = ante
				bank2.ante = ante
				break


def ask_keep(dice_list):
	'''
	Ask player to list the die/dice they want to keep. Any capitalization and spacing should work. Repeats are ignored. 
	'''
	while True:
		kept_string = input(">> Which dice would you like to keep? (Enter comma separated - e.g. a,b,c) ")
		kept = [s.strip().upper() for s in kept_string.split(',')]
		if len(kept) == 0:
			print("You must select at least 1 die to keep! ")
		elif (set(kept) <= set(dice_list)) == False:
			print("You must select valid die/dice! ")
		else:
			return kept
			break


def player_turn(player, hand):
	'''
	Logic of one player's turn
	'''

	# Declare player n's turn

	print('\n' + player.name + "'s turn! \n")

	# Create 6 dice named A-F

	dice_letters = ['A', 'B', 'C', 'D', 'E', 'F']
	dice = []
	for letter in dice_letters:
		dice.append(Die())
	dice_dict = dict(zip(dice_letters, dice))

	# Roll and keep values until player's hand has 6 values

	while len(hand.rolls) < 6:
		input(">> Press Enter to roll. ")
		temp_rolls = {}

		# Show rolled dice with letter names

		dice_header = ''
		for die in dice_dict.keys():
			dice_header += ('    ' + die + '       ')
			temp_roll = dice_dict[die].roll()
			temp_rolls[die] = temp_roll
			#print(Roll(temp_roll))
		print(dice_header)
		bilge_dice_display_funcs.ndice(*temp_rolls.values())	



		# Show player's hand

		print('Your hand: ')
		# print(hand)
		hand.display_hand()

		# Ask player which dice to keep

		kept = ask_keep(dice_letters)

		# Add kept dice to player's hand

		for die in set(kept):
			hand.keep_roll(temp_rolls[die])

			# Remove kept dice from ones that are "rollable"
			dice_letters.remove(die)
			del dice_dict[die]

		# Show updated hand and score

		hand.calc_score()
		hand.display_hand()
		print(player.name + "'s score: " + str(hand.score))