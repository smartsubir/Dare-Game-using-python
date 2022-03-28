from os import sys
import random
from array import *
y = 0

print("\n\nWELCOME TO WORLD OF DARE. HAVE FUN. \n--------------------------------------")

arr = []
no_of_players = int(input("\nEnter the number of players: "))

while y < no_of_players:
	y += 1
	name = str(y)
	x = input("\nEnter the name of player" +name +": ")
	arr.append(x)

print("\nThe name(s) of the player(s) who are currently playing this game is/are: ")
print(arr)

def main():
	print("\nPress ENTER to see who have to do the DARE.")
	action1 = input()

	z = random.choice(arr)

	def den():
		print("Hey, "+z +" it's your turn. Choose any letter between A to Z to see your DARE.")

		action2 = input()

		if (action2 >= 'a' and action2 <='z') or (action2 >= 'A' and action2 <= 'Z'):
			print("\nYou have chosen "+ action2 + " and your Dare is: ")

		else:
			print("\n You have entered a WRONG input. Please try again.")	
			den()
	den()

	number = random.randint(1,30)
	if number == 1:
		print("Peel a banana using only your feet and toes.")
	if number == 2:
		print("Tell a joke or act something funny.")
	if number == 3:
		print("Eat a piece of dog or cat food.")
	if number == 4:
		print("Dance like a cowboy in front of your mom and dad")
	if number == 5:
		print("Tell a secret of yours.")
	if number == 6:
		print("Take a selfie while you putting your finger inside \nyour nose and upload it as your WhatsApp profile picture.")
	if number == 7:
		print("Allow your gamming friends to ask you whatever they \nwant and you have to answer it truly.")
	if number == 8:
		print("Smear peanut butter all over your face.")
	if number == 9:
		print("Full your mouth with water and singing a song.")
	if number == 10:
		print("Do 10 push-ups.")
	if number == 11:
		print("Sing a Rap song.")
	if number == 12:
		print("Stand up on your ONE leg without any other supports for 20 seconds.")
	if number == 13:
		print("Smell a dirty sock for 10 seconds.")
	if number == 14:
		print("Act like Nana Patekar.")
	if number == 15:
		print("Do a model runway walk.")
	if number == 16:
		print("Eat a teaspoon of Dry Green tea or Soy sauce.")
	if number == 17:
		print("Tell your Secret wish.")
	if number == 18:
		print("Howl like a wolf for 10 seconds.")
	if number == 19:
		print("Let someone else style your hair and keep it that way for the rest of the game.")
	if number == 20:
		print("Spin around 10 times and try to walk straight.")
	if number == 21:
		print("Rub your friends armpits and then smell your fingers.")
	if number == 22:
		print("Do 20 situps.")
	if number == 23:
		print("Make fart noises with your armpit.")
	if number == 24:
		print("Keep your eyes open for 30 seconds without blinking.")
	if number == 25:
		print("Tell 5 sentences on cow but replace 'Cow' with 'I'.")
	if number == 26:
		print("Sing your Favorite song by tapping your nose with two fingers.")
	if number == 27:
		print("Dubbing your Favorite actor or actress.")
	if number == 28:
		print("Write 'I'm Pregnant' on your WhatsApp status and set it as public." )
	if number == 29:
		print("Slap harder yourself on the face.")
	if number == 30:
		print("Do plank for 1 mins.")

	print("\n Press ENTER to CONTINUE the GAME. \nPress 'Q', if you want to QUIT the GAME.\n")
	action3 = input()
	if action3 ==('q' or 'Q'):
		sys.exit(0)
	else:
		main()
main()

