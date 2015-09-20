
class A:
	def __init__(self):
		self.a = "legend"
		self.b = "hello"
		self.c = "world"
	def __str__(self):
		ret = ''
		for k,v in vars(self).items():
			ret += k
			ret += ':'
			ret += v
			ret += '\n'
		return ret;

if __name__ == "__main__":
	a = A()
	s = a.__str__()
	print s
