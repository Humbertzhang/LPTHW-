#-coding:utf-8--
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." %(age,height,weight)

#关于 input() 与 raw_input()  (可以用 type() 来查看一个输出的类型)
#用TYPR() 发现，input()会根据输入的不同而改变类型，如输入字符串是字符串类型(str)
#输入整数是整形(int)  而raw_input() 无论输入什么都会是字符串类型
# 可见于 http://jingyan.baidu.com/article/8ebacdf0db626749f65cd5f1.html

#第一题 raw_input 实现的是你输入一个东西，都会以字符串形式输出出来
#第三题

print "What's the color of your eyes?"
eyes_color= raw_input()
print "What's your hobby?"
hobby= raw_input()
print "What's your favourite color?"
color= raw_input()

print "So your erys' color is %r ," % eyes_color
print "your hobby is %r," % hobby
print "and your favourite color is %r." % color





















