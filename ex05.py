#--coding:utf-8--
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "He's %d pounds heavy." %weight
print "Actually taht's not too heavy."
#两个或以上的格式化字符需要用括号括起来，括号前面加%。
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are uaually %s depending on the coffee." %teeth
#this line is tricky , try to get it exactly right
print "If I add %d,%d,and %d I get %d." %(age,height,weight,age+height+weight) 




#格式化字符表

#描述


#   %% 百分号标记 
#   %c 字符及其ASCII码 
#   %s 字符串 
#   %d 有符号整数(十进制) 
#   %u 无符号整数(十进制) 
#   %o 无符号整数(八进制) 
#   %x 无符号整数(十六进制) 
#   %X 无符号整数(十六进制大写字符) 
#   %e 浮点数字(科学计数法) 
#   %E 浮点数字(科学计数法，用E代替e) 
#   %f 浮点数字(用小数点符号) 
#   %g 浮点数字(根据值的大小采用%e或%f) 
#   %G 浮点数字(类似于%g) 
#   %p 指针(用十六进制打印值的内存地址) 
#   %n 存储输出字符的数量放进参数列表的下一个变量中 
#   %r 书上提及的，可以用来显示任何东西。

a= 10.0008764
print "%r" %a

#   在python中，所有东西都可以转换成string类型，因此，如果没有什么特殊需求完全可以全部使用’%s‘来标记。

#   上面说的只是格式标记的最简间的形式，来看复杂一点的：

#   •‘%6.2f’ % 1.235
#   在这种形式中，在f的前面出现了一个类似小数的6.2它表示的意思是，总共输出的长度为6个字符，其中小数2位。还有更复杂的：
#   •‘%06.2f’ % 1.235
#   在6的前面多了一个0,表示如果输出的位数不足6位就用0补足6位。这一行的输出为‘001.24’，可以看到小数也占用一位。
#   类似于这里0这样的标记还有-、+。其中，-表示左对齐，+表示在正数前面也标上+号，默认是不加的。
#   有时候在%6.2f这种形式中，6和2也不能事先指定，会在程序运行过程中再产生，那怎么输入呢，当然不能用%%d.%df或%d.%d%f。可以用%*.*f的形式，
#   当然在后面的”要输出的值组“中包含那两个*的值。比如：'%*.*f' % (6, 2, 2.345)就相当于'%6.2f' % 2.345。
 

