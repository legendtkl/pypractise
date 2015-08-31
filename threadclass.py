import threading, time
from time import sleep,ctime

def now():
	return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

class myThread(threading.Thread):
	def __init__(self, nloop, nsec):
		super(myThread, self).__init__()
		self.nloop = nloop
		self.nsec = nsec

	def run(self):
		print 'start loop', self.nloop, 'at:', ctime()
		sleep(self.nsec)
		print 'loop', self.nloop, 'done at:', ctime()

def main():
	thpool=[]
	print 'starting at:', now()

	for i in xrange(10):
		thpool.append(myThread(i,2))

	for th in thpool:
		th.start()

	for th in thpool:
		th.join()
	print 'all done at:', now()

if __name__ == '__main__':
	main()
