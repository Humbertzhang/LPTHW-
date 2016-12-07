#--coding:utf-8--
x= "There are %d types of people." %10
#格式化字符还可以用来直接引用数字
binary="binary"
do_not="don't"
y="Those who know %s and those who %s."%(binary,do_not)  #字符串包含字符串1 #字符串包含字符串2

print x
print y 
print "I said :%r" %x     #字符串包含字符串3
print "I also said : '%s'."%y  #字符串包含字符串4

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious   
#格式化字符可以在一个字符串中出现后，在另一行以被宣称过的变量的形式再选择该格式化字符所表示的东西

w="This is the left side of..."
e="a string with a right side"
print w+e 