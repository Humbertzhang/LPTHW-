#-coding:utf-8--
from sys import argv
from os.path import exists

scirpt,from_file,to_file=argv

print "Copying from %s to %s" % (from_file,to_file)  #此处忘了%了= =

#we could do these two on one line too,how?
input= open(from_file)
indata= input.read()

print "The input file is %d bytes long" %len(indata)

print "Dose the output file exist? %r" %exists(to_file)
print "Ready,hit Enter to continue,Ctrl+c to abort."
raw_input(">")

output = open(to_file,'w')
output.write(indata)  #必须用indata 而不能用input ？ 只有读了才能write吗？
print "Alright , all done."

output.close()
input.close()

#第五题 cat 的替代品 type
#close 的作用：使文件关闭，不在读取或者写入东西
