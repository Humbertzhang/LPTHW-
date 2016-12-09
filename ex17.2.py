#-coding:utf-8--
from_file=raw_input()
input=open(from_file)
indata=input.read()
to_file=raw_input()
output=open(to_file,'w')
output.write(indata)