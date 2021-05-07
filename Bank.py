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