def greet(**kwargs):
	for k, v in kwargs.items():
		print "{0}=={1}".format(k,v)

greet(kelu="hello")
