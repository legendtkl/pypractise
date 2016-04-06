class Parent():
	def hello(self):
		print 'hello, parent'

class Child(Parent):
	def hello(self):
		print 'I am child'
		super(Child, self).hello()

hi = Child()
hi.hello()
