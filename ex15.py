#-coding:utf-8--
from sys import argv

script,filename=argv

txt = open(filename) #此处的filename即是你想打开的txt文件

print "Here's your file %r:" % filename  
#此处把你打开的文件的名字打印出来，与上面不同的是只作为名字出现
print txt.read()
#txt已经打开了文件，此处用read命令来指导它来干什么 
#read 可以读取TXT文件里面的东西
txt.close()  
print "Type the filename again:"
file_again = raw_input(">")
#此处还是输你想打开的txt文件
txt_again=open (file_again)

print txt_again.read()

#python open 的模式
#open ('C:\LPTHW\ex15add.txt','r') 为以READ模式打开，如果以w模式打开
#会使文件清空 
#更多关于open函数：
#http://www.360doc.com/content/14/0425/12/16044571_372066859.shtml






