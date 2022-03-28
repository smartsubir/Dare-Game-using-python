import random
numofguesses = 0

print("Hello!, What is your name:")
name = input()

number = random.randint(1,20)
print("Number I am thinking of is between 1 and 20 " , name)

while numofguesses < 6:
	print("take a guess. ")
	guess = input()
	guess = int(guess)

	numofguesses = numofguesses + 1
	if guess < number:
		print("number is too Low")
	if guess > number:
		print("number is too High")
	if guess == number:
		break
if guess == number:
	numofguesses = str(numofguesses)
	print("well done " ,name , "you guessed the number in: " , numofguesses)

if guess != number:
	number = str(number)
	print("wrong! unlucky, the number was: " ,number)
