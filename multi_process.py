import multiprocessing
import time

def worker1(interval):
	print "worker 1"
	time.sleep(interval)
	print "end worker 1"

def worker2(interval):
	print "worker 2"
	time.sleep(interval)
	print "end worker 2"

def worker3(interval):
	print "worker 3"
	time.sleep(interval)
	print "end worker 3"


if __name__ == "__main__":
	p1 = multiprocessing.Process(target=worker1, args=(2,))
	p2 = multiprocessing.Process(target=worker2, args=(3,))
	p3 = multiprocessing.Process(target=worker3, args=(4,))

	p1.start()
	p2.start()
	p3.start()

	print ("The number of CPU is: "+str(multiprocessing.cpu_count()))
	for p in multiprocessing.active_children():
		print ("child p.name:"+p.name+"\tp.id"+str(p.pid))
	print "END..."
