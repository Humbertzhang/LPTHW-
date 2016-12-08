#-coding:utf-8--
from sys import argv

script,user_name=argv
prompt='>'

print "Hi %s,I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s ?"% user_name
likes= raw_input(prompt) 

# 因为在定义 prompt 时有了引号所以在这里不用引号了

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer= raw_input(prompt)

print """   
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
"""  %(likes, lives, computer)
#  第一个  """ 必须与print 处于同一行








