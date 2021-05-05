import unittest
import io
import sys
import bilge_dice


## Test Classes and Methods

class TestRoll(unittest.TestCase):

	# Check that a Roll created with a face value of 4 has a value of 4
	def test_roll_creation(self):
		face = 4
		result = bilge_dice.Roll(face)
		self.assertEqual(result.value, face)


class TestDie(unittest.TestCase):

	# Check that each face of a Die is <= 6
	def test_die_creation(self):
		result = bilge_dice.Die()
		for face in result.die:
			self.assertLessEqual(face.value, 6)

	# Check that a roll of a Die is <= 6
	def test_die_roll(self):
		die = bilge_dice.Die()
		result = die.roll()
		self.assertLessEqual(result,6)


class TestPlayer(unittest.TestCase):

	# Check that a Player created with a name has that name attribute
	def test_player_creation(self):
		name = 'test player'
		result = bilge_dice.Player(name)
		self.assertEqual(result.name, name)


class TestHand(unittest.TestCase):

	# Check that a Hand created with a player has that player attribute, as well as an initial score of 0
	def test_hand_creation(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		result = bilge_dice.Hand(player)
		self.assertEqual(result.player, player)
		self.assertEqual(result.score, 0)

	# Check that a Hand has 3 values after 3 dice are rolled and kept
	def test_hand_keep_roll(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		result = bilge_dice.Hand(player)
		die_a = bilge_dice.Die()
		die_b = bilge_dice.Die()
		die_c = bilge_dice.Die()
		result.keep_roll(die_a.roll())
		result.keep_roll(die_b.roll())
		result.keep_roll(die_c.roll())

		self.assertEqual(len(result.rolls), 3)

	# Check that an empty hand is displayed as "[empty]"
	def test_hand_display_hand_empty(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		hand = bilge_dice.Hand(player)
		result = io.StringIO()
		sys.stdout = result
		hand.display_hand()
		result = result.getvalue().rstrip()
		self.assertEqual(result, '[empty]')


	# Check that the number of pips displayed matches the value of a non-empty hand
	def test_hand_display_hand_not_empty(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		hand = bilge_dice.Hand(player)
		die_a = bilge_dice.Die()
		die_b = bilge_dice.Die()
		hand.keep_roll(die_a.roll())
		hand.keep_roll(die_a.roll())
		result = io.StringIO()
		sys.stdout = result
		hand.display_hand()
		result = result.getvalue().rstrip()
		self.assertEqual(result.count('o'), sum(hand.rolls))


	# Check that Hand.qualified() returns boolean False after 1 roll
	def test_hand_qualified(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		hand = bilge_dice.Hand(player)
		die_a = bilge_dice.Die()
		hand.keep_roll(die_a.roll())
		result = hand.qualified()
		self.assertEqual(result, False)


	# Check that Hand.calc_score() returns 0 after 1 roll, and varied behavior after 3 rolls based on qualification
	def test_hand_calc_score(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		hand = bilge_dice.Hand(player)
		die_a = bilge_dice.Die()
		hand.keep_roll(die_a.roll())
		hand.calc_score()
		result = hand.score
		#self.assertEqual(result, 0)
		die_b = bilge_dice.Die()
		die_c = bilge_dice.Die()
		die_d = bilge_dice.Die()
		hand.keep_roll(die_b.roll())
		hand.keep_roll(die_c.roll())
		hand.calc_score()
		result = hand.score
		if 1 in hand.rolls and 4 in hand.rolls:
			self.assertIn(result, hand.rolls)
		else:
			self.assertEqual(result, 0)



class TestBank(unittest.TestCase):

	# Check that a Bank created with a player has that player attribute, as well as an initial ante of 0
	def test_bank_creation(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		result = bilge_dice.Bank(player)
		self.assertEqual(result.player, player)
		self.assertEqual(result.ante, 0)

	# Check that a Bank's total increases by the ante after a win, and ante resets
	def test_bank_win(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		result = bilge_dice.Bank(player)
		initial_total = result.total
		ante = 10
		result.ante = ante
		result.win()
		self.assertEqual(initial_total+ante, result.total)
		self.assertEqual(result.ante, 0)

	# Check that a Bank's total decreases by the ante after a loss, and ante resets
	def test_bank_lose(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		result = bilge_dice.Bank(player)
		initial_total = result.total
		ante = 10
		result.ante = ante
		result.lose()
		self.assertEqual(initial_total-ante, result.total)
		self.assertEqual(result.ante, 0)

	# Check that a Bank's total stays the same after a tie, and ante resets
	def test_bank_tie(self):
		name = 'test player'
		player = bilge_dice.Player(name)
		result = bilge_dice.Bank(player)
		initial_total = result.total
		ante = 10
		result.ante = ante
		result.tie()
		self.assertEqual(initial_total, result.total)
		self.assertEqual(result.ante, 0)




if __name__ == '__main__':
    unittest.main()








