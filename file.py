__author__ = "legendtkl"

if __name__ == "__main__":
	file_name = raw_input('Enter file name: ')
	f = open(file_name, 'w+')
	f.write('test line 1\n')
	for each in f:
		print each
	f.close()
	#or like below
	'''
	alllines = f.readlines()
	f.close()
	for each in alllines:
		print each
	'''
