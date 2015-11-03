def get_generator():
	for i in range(1000):
		yield i

if __name__ == '__main__':
	for i in get_generator():
		print i
