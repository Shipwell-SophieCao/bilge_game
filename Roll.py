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