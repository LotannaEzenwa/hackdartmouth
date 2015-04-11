import web
from bad_storage import *

urls = (
    '/(.*)', 'main'
    '/register(.*)', 'register'
)

app = web.application(urls, globals())

class register:        
	def POST(self, args):
		users = load_users() # REPLACE LATER
		name = list(users)
		if not name: 
			name = 'World'
		return 'Hello, ' + name + '!'

if __name__ == "__main__":
	app.run()