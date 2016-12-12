#-coding:utf-8--
#creat a mapping of state to abbreviation
states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

#create a basic set of states and some cities in them.
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland' #向city字典内加元素

# print out some cities
print '1' * 10
print "NY State has:",cities['NY']
print "OR State has:",cities['OR'] #输出字典时，用字典名+['字典左边的内容'] = 右边的

#print some states
print '2' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '3' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]  #内部的字典用来写出简称，配合外部的字典输出城市

#print every state abbreviation
print '4' * 10
for state,abbrev in states.items():  #此处即定义了state,abbrev 分别为字典中的前一列与后一列
	print "%s is abbreviated %s" %(state,abbrev)
	
#print every city in state
print '5' * 10
for abbrev,city in cities.items():
	print "%s has the city %s and %s" %(abbrev,city)

#Now do both at the same time
print '6' * 10
for state,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])
	
print '7' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
	print "Sorry,no Texas"
	
#get a city with a default values
city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: %s" %city





























