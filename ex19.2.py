def humbert(lo,li,ta): 
    print "I have %d apples\n" % lo
    print "I have %d bananas\n" % li
    print "I have %d pears\n" % ta
	# ":" should not be fogotten
	
#way1
humbert(1,1,1)
#way2
humbert(1+1,2+2,3+4)
#way3
lo=1 
li=2
ta=3
humbert(lo,li,ta)
#way4
humbert(lo+111,li+222,ta+333)
#way5
Lo=raw_input("Lo=")
Li=raw_input("Li=")
Ta=raw_input("Ta=")
humbert(lo,li,ta)


