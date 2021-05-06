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