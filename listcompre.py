L = [-1,1,2,3,4,5]

def f(x):
	return x+1;

def g(x):
	return x*x;

print [g(f(i)) for i in L]
