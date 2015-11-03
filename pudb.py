import pudb; pu.db

def fib(x):
	if x == 0:
		return 1
	elif x == 1:
		return 2
	else:
		return fib(x-1)+fib(x-2)

def error():
	print 'hello'

if __name__ == "__main__":
	print error(1)
	print fib(2)
	print fib(3)
	print fib(10)
