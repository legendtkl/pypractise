import threading, Queue
import time

exitFlag = False

class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args
	
	def run(self):
		print 'starting', self.name, 'at:', time.ctime()
		apply(self.func, self.args)
		print 'finished', self.name, 'at:', time.ctime()


def writer(queue, x):
	global exitFlag
	for i in range(100):
		queue.put(i, 1)
	exitFlag = True


def reader(queue, x):
	global exitFlag
	while queue.empty() == False or exitFlag == False:
		val = queue.get(1)
		print 'Q size:', queue.qsize(), 'Q empty:', queue.empty(), 'exitFlag:', exitFlag
		print 'Reading', val, '...Done'

def main():
	q = Queue.Queue(10)
	t1 = MyThread(writer, (q,1), 'writer')
	t2 = MyThread(reader, (q,1), 'reader')
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	print 'All Done!'

if __name__ == '__main__':
	main()
