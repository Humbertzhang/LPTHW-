#--coding:utf-8--
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat ="I'm \\ a \\ cat."

fat_cat= '''
I'll do a list :
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
\a
\a 
'''
#三个'''与三个"""效果一样 
# \a 可以让发出响声

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#第一题

#转义字符
#描述


#   \(在行尾时) 续行符 
#   \\ 反斜杠符号 
#   \' 单引号 
#   \" 双引号 
#   \a 响铃 
#   \b 退格(Backspace) 
#   \e 转义 
#   \000 空 
#   \n 换行 
#   \v 纵向制表符 
#   \t 横向制表符 
#   \r 回车 
#   \f 换页 
#   \oyy 八进制数yy代表的字符，例如：\o12代表换行 
#   \xyy 十进制数yy代表的字符，例如：\x0a代表换行 
#   \other 其它的字符以普通格式输出 

#第三题
r=100.00 
print "\"%f\"" %r   
                     #可以用\\在字符串中表示\
                     #在引用%时，，一定要记住格式为 print "%r" ,%变量
					 
#第四题
a="\"A B C D E F G\""
print "%r" %a
print "%s" %a

#%r展示你写的东西 %s 展示你应该看到的东西





