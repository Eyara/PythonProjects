from bs4 import BeautifulSoup
from urllib import request
import re

token = '247140900:AAGLfo4W2OoAKn2kJpEJTCDgpLiDCi1Oiog'

def FindQuestion():
	doc = request.urlopen('http://db.chgk.info/random/answers/types1/').read()
	soup = BeautifulSoup(doc, "lxml")
	question = soup.find("div", class_= "random_question")
	question.div.decompose()
	question.p.decompose()
	result = re.split(r'<strong>', str(question))
	question = result[1]
	answer = result[2]
	question = question.replace('</strong>', ' ')
	question = question.replace('<p>', ' ')
	question = question.replace('<br/>', ' ')
	answer = answer.replace('</strong>', ' ')
	answer = answer.replace('</p>', ' ')
	answer = answer.replace('<p>', ' ')
	answer = answer.replace('<br/>', ' ')
	answer = answer.replace('</div>', ' ')
	result = question + answer 
	print (result)
	return result
