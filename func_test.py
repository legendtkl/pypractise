__author__ = "legendtkl"

def shout(word="yes"):
	return word.capitalize()+"!"

def talk():
	def whisper(word="talk little"):
		return word.lower()+"..."
	print whisper()

talk()
'''
scream = shout

print shout()
del shout
print scream("fuck")
'''
