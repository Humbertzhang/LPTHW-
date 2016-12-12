#-coding:utf-8--
from sys import exit
def Sphinx_room():	
	print "There's a sphinx in this room."
	print "You have to answer its questions rightly."
	print "OR, You will die."
	print "Are you ready?"
	choice = raw_input("> ")
	
	if choice == "Yes":
		print "Sphinx: There's an animals."
		print "Sphinx: It can walk in 4 legs at moring."
		print "Sphinx: Walk in 2 legs at noon."
		print "Sphinx: While walk in 3 legs at night."
		print "Sphinx: Who are it?"
		answer=raw_input("> ")
		if answer == "Human":
			print "Sphinx: You are right!I can't believe it.And I will die!!!"
			print "Sphinx jumps into a river and it dies."
			print "You win!You have beaten 3 monsters. You are the king!"
			exit(0)
		else :
			print "sphinx: You are wrong,the answer is human."
			print "sphinx eats your head."
			print "You die"
			exit(0)
	else :
		print "Alright,maybe next time."
		Sphinx_room()
		
def Cerberus_room():
	print "There's a cute dog."
	print "Maybe not that cute, as it has three heads and some shape teeth."
	print "What should you do?"
	dog_sleep = False
	while True:  #这个True 条件只是为了能一直制造循环。

		choice = raw_input(">bet?chicken?poison? ")
		if choice == "bet" and not dog_sleep :
			dead("The dog attack you! You are dead.")
		elif choice == "bet" and dog_sleep :
			print "The dog is killed by you,good job,my youth."
			Sphinx_room()
		elif choice == "chicken":
			print "The dog eat the chicken,and it fall in sleep."
			dog_sleep = True
		elif choice == "poison" :
			print "The dog is killed by you,good job,my youth."
			Sphinx_room()
		else :
			print "I got no idea what that means."
	
			
def Gorgons_room() :
	print "You walk in the new rood."
	print "Suddenly,You find a stone in you left."
	print "Thers some words on it."
	print "Stone : There are some monsters here."
	print "Stone : If you want to go out alive , you should kill them all.\nAnd You will become the next king.\n"
	print "Stone : The first monster is the Gorgons.You can never look at her.\nOR you will become a stone...like ME!!"
	print "You notice there is a bomb at the stone's feet."
	print "Do you want to pick it up?"
	
	bomb = raw_input("> ")
	if bomb == "Yes":
		print "You get the item : Bomb."
		bomb = True
	elif bomb == "No":
		print "You should take it the next time!"
		bomb = False
	else :
		dead("The bomb bombs.You are dead.")
	
	print "You walk again,and you notice a cave again.\nyou find there are many stones here"
	print "You here someone in the cave is coming out of it."
	print "You konw She? is Gorgon sisters."
	print "Do you have bomb?"
	use = raw_input("> ")
	
	if use == "Yes" and bomb:
		print "You through the bomb into the cave.She is dead"
		print "You killed the first monster"
		print "You walk again."
		Cerberus_room()
	else :
		print "You see the monsters and She is that beautiful that you want to see her forever"
		dead("You become a stone")
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
		
def start():
	print "You walk in a rood and you notice a cave."
	print "You enter that cave without think about it."
	print "You walk a long time before you out."
	print "When you walk out of the cave,You find you are in a new world."
	print "Are you ready?"
	ready = raw_input("> ")
	if ready == "Yes":
		Gorgons_room()
	elif ready == "dog":
		Cerberus_room()
	elif ready == "lion":
		Sphinx_room()
	else :
		dead("You were killed by a stone from the sky")
	
start()	