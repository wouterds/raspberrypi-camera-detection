import cherrypy

cherrypy.config.update({
	'server.socket_host': '0.0.0.0',
	'server.socket_port': 3000,
})

class WebServer(object):

	@cherrypy.expose
	def index(self):
		IP = cherrypy.request.remote.ip
		HTML = "Hello, " + IP
		return HTML

cherrypy.quickstart(WebServer())
