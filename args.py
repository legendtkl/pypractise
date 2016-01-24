def func_var_args(farg, *args):
	print "arg:", farg
	for value in args:
		print "another arg:", value

def func_var_kwargs(farg, **kwargs):
	print "arg:", farg
	for key in kwargs:
		print "key, value: %s, %s" % (key, kwargs[key])

if __name__ == '__main__':
	func_var_args(1, "two", 3)
	func_var_kwargs(farg=0, a=1, b="two", c=3.0)
