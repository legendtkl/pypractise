import web

urls = (
	'/', 'hello',
	'/tkl', 'world'
)


class hello:
	def GET(self, name):
		if not name:
			name = 'World'
		return 'hello, ' + name + '!'
	def POST(self):
		data = web.data()
		return data
class world:
	def POST(self):
		data = web.data()
		return 'hello, ' + data

if __name__ == '__main__':
	app = web.application(urls, globals(), False)
	app.run()
