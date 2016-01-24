class Legend:
	def __getitem__(self, key):
		return self.__dict__[key]
	def __setitem__(self, key, value):
		self.__dict__[key] = value

class Product:
	name = {}
	def __init__(self, **args):
		for k, v in args.items():
			print k, v
			self.name[k] = v
	def __getitem__(self,k):
		return self.name[k]

		


if __name__ == '__main__':
	p = Product(name="abc")
	print p['name']
