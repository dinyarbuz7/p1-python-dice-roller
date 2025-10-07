import random
while True:
	choice = input("Do you wanna play?(y/n): ").lower()
	if choice == "y" :
		amount = int(input("How many dice do you wanna roll?: "))
		c = 0
		for i in range (amount):
			c+=1
			die1 =random.randint(1,6)
			die2 = random.randint(1,6)
			print(f'({die1}, {die2})', f'Number of dice rolled: {c}', sep="\n")
	elif choice == "n":
		print("OK, thank you!. Bye.")
		break
	else:
		print("Sorry, you can type only y or n", "Invalid choice", sep = "\n")
	
