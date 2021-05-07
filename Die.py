import random 
from Roll import Roll

# 6 sided die values

faces = [1, 2, 3, 4, 5, 6]

class Die:

	def __init__(self):
		self.die = []
		for face in faces:
			self.die.append(Roll(face))

	def roll(self):
		return random.choice(self.die).value