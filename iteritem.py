dict = {'z':5, 'x':3, 'y':4}
l = []
x1 = [1,2]
x2 = [2,3]
x3 = [3,4]
l.append(x1)
l.append(x2)
l.append(x3)

for k,v in dict.items():
	print k,v

for x in xrange(len(l)):
	print x, l[x][0], l[x][1]
