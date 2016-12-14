#-coding:utf-8--
class Parent(object):
	
	def override(self):
		print "PARENT override()"
	
	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):
	def override(self):
		print "CHILD override()"
	
	def altered(self):
		print "CHILD,BEFORE PARENT altered()"
		super(Child,self).altered()
		print "CHILD,AFTER PARENT altered()"
		
dad = Parent()
son = Child()

print "implicit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#隐性继承
dad.implicit()
son.implicit()

print "override!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#重写父类方法
dad.override()
son.override()

print "altered!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#在子类的重写的方法中加入父类原来的方法
dad.altered()
son.altered()
	
	
	
	
	
	
	
	
	
	
	
	
	