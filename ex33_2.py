#-coding:utf-8--
lolita = input ("What number do u want?:")
numbers=[]
i=0
a = input ("What number do u want to add?:")
def Humbert(lolita):
	global i
	while i < lolita :
		print "At the top i is %d" %i 
		numbers.append(i)
		i=i+a
		print "Numbers now:",numbers
		print "At the bottom i is %d" %i 
    
Humbert(lolita)

print "The numbers:"
for num in numbers:
	print num 

	
