# Welcome to Bilge Dice! 

_Inspired by a [long lost Neopets game](http://www.jellyneo.net/?go=bilge_dice)_

## Getting Started: 

- Clone project
```bash
git clone https://github.com/Shipwell-SophieCao/bilge_game.git "Bilge Dice"
```

- Import packages
```python
import random
```

- Run from the command line
```bash
python bilge_dice.py
```

- Game rules

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
	- You can play again if neither player is bankrupt :smile:

## Updates:

- 3/29/21 git remote update: 
```bash
git remote rename python-learning bilge_game
```