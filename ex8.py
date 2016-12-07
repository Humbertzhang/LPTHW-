#--coding:utf-8--
formatter="%r%r%r%r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,False,True) #True 与 False 在python中不需要双引号
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
     "I had this thing.",
	 "That you could type up right.",
	 "But it didn't sing.",
	 "So I said goodnight."
)
#关于最后一行的单双引号，可能是因为在第三行中有单引号的存在才使得第三行打印出来外面是双引号
#如果外面没有双引号就打印为双引号