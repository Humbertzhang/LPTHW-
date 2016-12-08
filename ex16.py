#-coding:utf-8--
from sys import argv

script,filename=argv

print "We're going to erase %r." % filename
print "If you don't want that,hit Ctrl+C."
print "If you do want that , hit RETURN."

raw_input("?")

print "Opening the file..."
target=open(filename,'w') #以写的模式打开

print "Truncating the file . Goodbye~"
target.truncate()

print "Now, I'm going to ask you for three lines."

line1=raw_input("line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) #此处line1只是一个记号，并不是真的表示第一行，实现第一行用的是 \n 
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally , we close it."
target.close()