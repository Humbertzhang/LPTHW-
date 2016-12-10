#-coding:utf-8--
print "Now , you are coming to a bizarre world,Are u ready?"
ready= raw_input(">Yes? ")
if ready == "Yes" :
	print "Wow , you fall in a strange world ,and you die~"
else:
	print "Alright,let's come to the ordinary world."
	
	print "You weak up."
	print "Do you know your name?"
	name = raw_input (">")
	print "Yes! You are %s. You still remember it." % name
	
	print "Hey, %s, do u still remember what you have done before you come to here?"%name
	rem=raw_input("Yes?")
	if rem == "Yes" :
		print "You have a good mind ,so i'm going to kill you."
		print "You died, %s." %name
	else:
		print "You are welcome , I am you father,%s,maybe you can't remember it."%name
		print "Let me get you something to eat~"
		
		print "He brings three kinds of food."
		print "They are bread,apple and sandwich."
		print "What do you want to eat?"
		raw_input("The food I want to eat is:")
		print "Great! you are died! Brillant~"
	
	
	