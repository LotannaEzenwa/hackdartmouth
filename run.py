import sys
sys.path.insert(0, './python')
import web
from bad_storage import *

urls = (
	'/', 'index',
	'/register', 'register',
	'/(\d+)', 'page'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		# return 'hello world'
		if web.cookies().get('loggedin') == None:
			raise web.seeother('/static/index.html', 303)
		else:
			raise web.seeother('/1')

class register: 
	def GET(self):
		return 'hello world'    

	def POST(self):
		user_data = web.input()
		users = load_users() # REPLACE LATER
		users[user_data.username] = {'password': user_data.password, 'email': user_data.email}
		save_users(users)
		web.setcookie('loggedin', True, expires="", domain=None, secure=False)
		raise web.seeother('/')

class page:
	def GET(self, id):
		return 'thanks for accessing argument' + str(id)

if __name__ == "__main__":
	app.run()