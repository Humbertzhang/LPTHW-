#yong IF chongxingouzao 

i=0
numbers=[]

for i in range(7):
	if i != 0 :
		print "Numbers now:",numbers
		print "At the bottem i is %d" %i
	if i != 6 :
		print "At the top i is %d"%i
		numbers.append(i)

print "The numbers: "
for num in numbers:
	print num