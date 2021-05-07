import display_funcs
from Roll import Roll

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
			display_funcs.ndice(*self.rolls)

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