import cherrypy, subprocess, threading, time, Queue, logging, sys, json


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

log = {}

class MockServer(object):
	count = 0
	@cherrypy.expose
	def log(self, **kwargs):
		self.count = self.count + 1
		cherrypy.response.status = 200
		print 'response code: ', cherrypy.response.status
		transaction = {}
		log['transaction%s' % self.count] = transaction
		logger.info('transaction %s: {' % self.count)
		headers_log = ['User-Agent', 'Cookie']
		for key in headers_log:
			if key in cherrypy.request.headers.keys():
				logger.info(key + ': ' + cherrypy.request.headers[key])
				transaction[key] = cherrypy.request.headers[key]

		http_method = cherrypy.request.method
		if http_method == "GET":
			logger.info('url:http://localhost:%s/?'% CHERRYPY_PORT + cherrypy.request.query_string)
			transaction['url'] = 'http://localhost:%s' % CHERRYPY_PORT
				
		elif http_method == "POST":
			logger.info(cherrypy.request.body.params)
			print cherrypy.request.body.params
		logger.info('}')
		logger.info(json.dumps(log))
		print log
		print 'response code: ', cherrypy.response.status

if __name__ == '__main__':
	fh = logging.FileHandler('test2.log')
	fh.setLevel(logging.INFO)
	fh.setFormatter(logging.Formatter('%(message)s'))
	logger.addHandler(fh)
	subprocess.call('''lsof -i:%s | awk '{if($2!="PID") print $2}' | sort | uniq | xargs sudo kill -9''' % CHERRYPY_PORT, shell = True)
	d = cherrypy._cpdispatch.RoutesDispatcher()
	d.connect(name='log', route='/api/1/ingest/creatives', controller=MockServer(), action='log')
	conf = {'/': {'request.dispatch': d}}
	cherrypy.quickstart(MockServer(), '/', config=conf)
	cherrypy.quickstart(MockServer())

