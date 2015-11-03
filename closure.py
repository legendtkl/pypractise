def foo():
	n=1
	def inner():
		print n
	inner()
	n='x'
	inner()

if __name__ == "__main__":
	foo()
