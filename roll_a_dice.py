import random
def roll(num_of_dice):
	for i in range(num_of_dice):
		print(f"Dice {i+1} rolled a {random.randint(1,6)}.")
		
def play():
	c=int(input("Enter the number of dice : "))
	roll(c)
	ch=str(input("Continue?(Y/N)"))
	if ch=='Y':
		play()
play()
