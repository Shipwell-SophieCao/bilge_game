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

# 6 sided die values

faces = [1, 2, 3, 4, 5, 6]

# strings to print dice graphics

s = "+-------+"
m1 = "| o   o |"
m2 = "| o     |"
m3 = "|   o   |"
m4 = "|     o |"
m5 = "|       |"

dice_display = [
	[m5, m3, m5],
	[m2, m5, m4],
	[m2, m3, m4],
	[m1, m5, m1],
	[m1, m3, m1],
	[m1, m1, m1]
]


## Classes ##

class Roll:
	"""
	Defines possible outcomes of a die roll 1-6 with value and graphics
	"""
	def __init__(self, value):
		self.value = value

	# Directly print(Roll) for temp rolls (default black)
	def __str__(self):
		return '\n'.join(dice_display[self.value-1])
		

	# Use print_hand() method to display hand values in blue
	def print_hand(self):
		print(Fore.BLUE + '\n'.join(dice_display[self.value-1]))
		print(Style.RESET_ALL)


class Die:

	def __init__(self):
		self.die = []
		for face in faces:
			self.die.append(Roll(face))

	def roll(self):
		return random.choice(self.die).value


class Player:

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name


class Hand:

	def __init__(self, player):
		self.rolls = []
		self.score = 0
		self.player = player

	def keep_roll(self, roll):
		self.rolls.append(roll)

	def __str__(self):
		for roll in self.rolls:
			print(Roll(roll))
		return ''

	def display_hand(self):
		if len(self.rolls) == 0:
			print('[empty]')
		else:
			ndice(*self.rolls)

	def qualified(self):
		if 1 in self.rolls and 4 in self.rolls:
			return True
		else:
			return False

	def calc_score(self):
		if 1 in self.rolls and 4 in self.rolls:
			self.score = sum(self.rolls) - 5
		else:
			self.score = 0


class Bank:

	def __init__(self, player):
		self.player = player
		self.total = 100 
		self.ante = 0

	def win(self):
		self.total += self.ante
		self.ante = 0

	def lose(self):
		self.total -= self.ante
		self.ante = 0

	def tie(self):
		self.ante = 0

	def __str__(self):
		return self.player.name + ' has ' + str(self.total) + ' NP. '


## Test Classes ##

# die_a = Die()
# die_b = Die()
# die_c = Die()

# test_hand = Hand('test')
# test_hand.keep_roll(die_a.roll())
# test_hand.keep_roll(die_b.roll())
# test_hand.keep_roll(die_c.roll())
# print(test_hand)

# print(test_hand.qualified())
# test_hand.calc_score()
# print(test_hand.score)


## Functions ##

def die(i):
    return [s, *dice_display[i-1], s]

def join_row(*rows):
	'''
	Used for printing multiple dice horizontally vs. vertically
	'''
	return ['   '.join(r) for r in zip(*rows)]

def ndice(*ns):
	'''
	Used to print any number of dice horizontally
	'''
	for line in join_row(*map(die, ns)):
		print(line)


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
		ndice(*temp_rolls.values())	



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
		# print(hand)
		hand.display_hand()
		print(player.name + "'s score: " + str(hand.score))



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

	pick_ante(bank1, bank2)

	# Reset players' hands

	hand1 = Hand(player1)
	hand2 = Hand(player2)

	# Randomly decide who goes first (bc the 2nd player has an advantage)

	first = random.randint(1,2)

	if first == 1:
		player_turn(player1, hand1)
		player_turn(player2, hand2)
	else:
		player_turn(player2, hand2)
		player_turn(player1, hand1)

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









