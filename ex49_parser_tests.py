from nose.tools import *
from bin import parser

def test_peek():  
	word_list = [('noun','bird')]
	result = parser.peek(word_list)
	assert_equal((result),"noun")

def test_match():
	word_list = [('noun','bird'),('verb','tell')]
	expecting = ('noun')
	result = parser.match(word_list,expecting)
	assert_equal((result),('noun','bird')) #because the result's form is () ,so the later factor's form should be also ().


def test_parse_verb():
	word_list = [('verb','tell'),('noun','bird')]
	result = parser.parse_verb(word_list)
	assert_equal((result),('verb','tell'))

def test_parse_object():
	word_list = [('direction','north'),('verb','tell')]
	result = parser.parse_object(word_list)
	assert_equal((result),('direction','north'))

def test_parse_subject():
	word_list = [('noun','Humbert'),('direction','north'),('noun','bird')]
	result = parser.parse_subject(word_list)
	assert_equal((result),('noun','Humbert'))

