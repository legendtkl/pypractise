def take(seq, n):
	for i in xrange(n):
		yield seq.next()

L = (1,2,3,4,5,6,7,8)
while True:
	x = list(take(L, 2))
	print x
