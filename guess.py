import random
import pdb

random_num =random.randint(1,10)

# print("Guess the number from 1 to 10: ")
# guess = int(input())
# while guess != random_num:
# 	if guess > random_num:
# 		print("Too big, guess again: ")
# 		guess = int(input())
# 	elif guess < random_num:
# 		print("Too small, guess again: ")
# 		guess = int(input())

# print("You win!")


guess = int(input("Guess the number from 1 to 10: "))
while True:
	if guess == random_num:
		print(random_num)
		print("You win")
		break	
	else:
		guess = int(input("Guess again: "))

	pdb.set_trace()


	
