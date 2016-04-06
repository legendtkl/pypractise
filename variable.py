a = 1
def fun(a):
	a = 2
b = []
def func(b):
	b.append(3)

class Person:
	name = "aaa"
p1=Person()
p2=Person()
p1.name='bbb'

fun(a)
func(b)
print a
print b
print p1.name
print p2.name
print Person.name
