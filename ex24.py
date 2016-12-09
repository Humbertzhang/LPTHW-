#-coding:utf-8--
print "Let's practice everyting."
print "You\'d need to know \'bout escapes with\\ that do \n new lines and \t tabs."  
	   
#1,既可以用双引号又可以用单引号
#2，\为转义字符，可以把一些会被编译器理解的但却是你想打印出来的东西打出来
#3，\n 换行  \t 相当于一个 TAB 会有四个空格
#4，一个字符串不能在编辑器里换行

poem= """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""

print "-------------------"
print poem
print "-------------------"
#“”“ ”“” 可以一次定义许多字符串， 并且在其之中也可以用 \t \n %等命令

five = 10-2+3-6
print "This should be five : %s" %five
#格式化字符


def secret_formula(started):
	jelly_beans=started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates
	
start_point = 10000
beans,jars,crates = secret_formula(start_point) 
#即把 start_point 当做定义函数时的 started
#把 beans , jars , crates 分别附上 secret_formula 里的三个变量的值
#因为函数中的赋值命名与外界的符号的命名没有相关关系。

print "With a starting point of : %d" % start_point
print "We'd have %d beans,%d jars,and %d crates." %(beans,jars,crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans,%d jars,and %d crates." % secret_formula(start_point) 

#在已经赋完值得前提下，，利用格式化字符调用的两种方式