import cherrypy, subprocess, threading, time, Queue, logging, sys

'''
class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def getResult(self):
		return self.res

	def run(self):
		print 'starting', self.name, 'at:', time.ctime()
		self.res = apply(self.func, self.args)
		print self.name, 'finished at:', time.ctime()


exitFlag = False

def reader(queue, x):
	global exitFlag
	while queue.empty() == False or exitFlag == False:
		val = queue.get(1)
		print 'consumed object from Q'
'''

CHERRYPY_PORT = 8002
cherrypy.config.update({ 'server.socket_host':'127.0.0.1',
						'server.socket_port':CHERRYPY_PORT,})

logger = logging.getLogger('mylog')
logger.setLevel(logging.INFO)


def check_mockserver_state():
	return cherrypy.engine.state == cherrypy.engine.states.STARTED

def stop_mockserver():
	cherrypy.engine.exit()
	subprocess.call('''lsof -i:%s | awk '{if($2!="PID") print $2}' | sort | uniq | xargs sudo kill -9''' % CHERRYPY_PORT, shell = True)
	#subprocess.call('''netstat -apn | grep %s | awk '{print d$7}' | cut -d'/' -f 1 | xargs sudo kill -9''' % CHERRYPY_PORT, shell = True)

class MockServer(object):
	@cherrypy.expose
	def log(self, **kwargs):
		headers_log = ['User-Agent', 'Cookie']
		for key in headers_log:
			if key in cherrypy.request.headers.keys():
				logger.info(key + ': ' + cherrypy.request.headers[key])

		http_method = cherrypy.request.method
		if http_method == "GET":
			logger.info('http://localhost:%s/?'% CHERRYPY_PORT + cherrypy.request.query_string)
				
		elif http_method == "POST":
			logger.info(cherrypy.request.body.params)
			print cherrypy.request.body.params

if __name__ == '__main__':
	'''
	q = Queue.Queue(30)
	t1 = MyThread(reader, (q, 0), 'Reader')
	t2 = MyThread(cherrypy.quickstart, (MockServer, '/'), 'MockServer')
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	'''
	if len(sys.argv) != 2:
		sys.exit(0)
	base_dir = sys.argv[1]
	filename = base_dir +'/test.log'
	print filename
	fh = logging.FileHandler('test1.log')
	fh.setLevel(logging.INFO)
	fh.setFormatter(logging.Formatter('%(message)s'))
	logger.addHandler(fh)
	subprocess.call('''lsof -i:%s | awk '{if($2!="PID") print $2}' | sort | uniq | xargs sudo kill -9''' % CHERRYPY_PORT, shell = True)
	cherrypy.quickstart(MockServer())

