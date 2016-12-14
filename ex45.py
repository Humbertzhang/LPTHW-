#-coding:utf-8--
from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "Welcome , my warrior."
		print "This is another scene now."
		print "------------------------------------------------\n------------------------------------------------"

class Engine(object): 

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()
		
		

		
class Death(Scene):
	quips = [
	"You died.You kinda suck at this.",
	"Your mom would be proud...if she was smarter.",
	"Such a luser.",
	"I have a small puppy that's better at this."
	]
	def enter(self):
		print "You are dead man, it's COOOOOOOOOOOOOOOOOOL"
		print Death.quips[randint(0,len(self.quips)-1)] #生成随机数，来随机出现一个死亡时的话语
		exit(1)
		


class FightRoom(Scene):
	def enter(self):
		

		
		super(FightRoom,self).enter()
		print "You walk through the Sphinx's cave."
		print "When you walk out of it"
		global your_lives
		person = randint(3,8)
		your_lives = randint (499,999)
		print "You find there are %s person." % person
		print "They all armed to the teeth."
		print "You have to fight with them."
		global dead_guy 
		dead_guy = 0 
		while your_lives > 0 and dead_guy != person :
			
			their_attact = randint (15,45)
			your_lives = your_lives - person*their_attact
			print "You lives is %d now" % your_lives
			dead_guy = dead_guy + 1
			print "dead guy is : %d now" % dead_guy 
			print "%r guys is dead by your attack." %dead_guy
		
		if your_lives > 0 :
			return 'finished'
			
		else :
			return 'death'

		
class SphinxRoom(Scene):	
	def enter(self):
		super(SphinxRoom,self).enter()
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
				return 'Fight_'
			else :
				print "sphinx: You are wrong,the answer is human."
				print "sphinx eats your head."
				return 'death'
		else :
			print "Alright,maybe next time."
			return 'Sphinx_'
				
class CerberusRoom(Scene):
	def enter(self):
		super(CerberusRoom,self).enter()
		print "There's a cute dog."
		print "Maybe not that cute, as it has three heads and some shape teeth."
		print "What should you do?"
		dog_sleep = False
		while True:  #这个True 条件只是为了能一直制造循环。
			
			choice = raw_input(">bet?chicken?poison? ")
			if choice == "bet" and not dog_sleep :
				print "The dog attack you! You are dead."
				return 'death'
			elif choice == "bet" and dog_sleep :
				print "The dog is killed by you,good job,my youth."
				return 'Sphinx_'
			elif choice == "chicken":
				print "The dog eat the chicken,and it fall in sleep."
				dog_sleep = True
			elif choice == "poison" :
				print "The dog is killed by you,good job,my youth."
				return 'Sphinx_'
			else :
				print "I got no idea what that means."
				
class GorgonsRoom(Scene):
	def enter(self):
		super(GorgonsRoom,self).enter()
		print "You walk in the new rood."
		print "Suddenly,You find a stone in you left."
		print "Theres some words on it."
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
			return 'death'
		
		print "You walk again,and you notice a cave again.\nyou find there are many stones here"
		print "You here someone in the cave is coming out of it."
		print "You konw She? is Gorgon sisters."
		print "Do you have bomb?"
		use = raw_input("> ")
	
		if use == "Yes" and bomb:
			print "You through the bomb into the cave.She is dead"
			print "You killed the first monster"
			print "You walk again."
			return 'Cerberus_'
		else :
			print "You see the monsters and She is that beautiful that you want to see her forever"
			dead("You become a stone")
			return 'death'
class Start(Scene):
	def enter(self):
		super(Start,self).enter()
		print "You walk in a rood and you notice a cave."
		print "You enter that cave without think about it."
		print "You walk a long time before you out."
		print "When you walk out of the cave,You find you are in a new world."
		print "Are you ready?"
		ready = raw_input("> ")
		if ready == "Yes":
			return 'Gorgons_'
		elif ready == "dog":
			return 'Cerberus_'
		elif ready == 'lion':
			return 'Sphinx_'
		elif ready == 'gays':
			return 'Fight_'
		else :
			return 'death'
			
class Finished(Scene):

    def enter(self):
        print "You won! Good job.\nWooooooooooooooooooooow,I Finished This Game."
        return 'finished'
		
class Map(object):

	scenes = {
	'Sphinx_':SphinxRoom(),
	'Cerberus_':CerberusRoom(),
	'Gorgons_':GorgonsRoom(),  
	'Fight_':FightRoom(), 
	'start_':Start(),	
	'death':Death(),
	'finished':Finished(),
	}
	def __init__(self,start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('start_')
a_game = Engine(a_map)
a_game.play()		
	