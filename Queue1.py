import Queue, threading, time

exitFlag = 0

class myThread (threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	def run(self):
		print "Starting " + self.name
		process_data(self.name, self.q)
		print "Exiting " + self.name

def process_data(threadName, q):
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data q.get()



threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1
