#-coding:utf-8--
ten_things = "Apple Oranges Crows Telephone Light Sugar"

print "Wait there's not ten things in that list,let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()  #pop函数用来移除more_stuff列表里的一个元素 |默认最后一个|
	print "Adding: ",next_one
	stuff.append(next_one)
	print "There's %d items now." %len(stuff)

print "There we go: ",stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] 
print stuff.pop()
print ' '.join(stuff) #what? cool!
print '#'.join(stuff[3:5]) #super stellar  连接第三个和第五个
#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。