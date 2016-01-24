class Legend():
	def update(self, _obj):
		self.__dict__.update(_obj)

if __name__ == '__main__':
	tkl = Legend()
	a = 'abc'
	tkl.update(a)

	print tkl.a
