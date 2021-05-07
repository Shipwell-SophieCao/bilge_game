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
import display_funcs
from Roll import Roll
from Die import Die
from Player import Player
from Hand import Hand
from Bank import Bank
import game_funcs


## Run the Game ##

game_funcs.play_dice()





