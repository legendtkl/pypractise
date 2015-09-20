def foo():
	L = [1,2,3,4]
	for i in L:
		if i==2:
			return
		elif i==1:
			print 'i==1'
		else:
			print i
		print 'hello world'

if __name__ == "__main__":
	foo()
