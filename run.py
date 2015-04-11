import sys
sys.path.insert(0, './python')
import web
import json
from bad_storage import *

urls = (
	'/', 'Index',
	'/register', 'Register',
	'/login', 'Login',
	'/(\d+)', 'Page',
	'/add_argument','Add_Argument',
	'/get_argument', 'Get_Argument',
	'/vote', 'Vote'
)

app = web.application(urls, globals())

class Index:
	def GET(self):
		users = load_users() # REPLACE LATER
		if not web.cookies().get('loggedin') in users:
			raise web.seeother('/static/index.html', 303)
		else:
			raise web.seeother('/1')

class Register: 
	def POST(self):
		user_data = web.input()
		users = load_users() # REPLACE LATER
		users[user_data.username] = {'password': user_data.password, 'email': user_data.email}
		save_users(users) # REPLACE LATER
		web.setcookie('loggedin', user_data.username, expires="", domain=None, secure=False)
		raise web.seeother('/')

class Login:
	def LOGIN(self):
		user_data = web.input()
		users = load_users() # REPLACE LATER
		good_user = False
		if user_data.username in users:
			if user_data.password == users[user_data.username]:
				good_user = True

		if good_user:
			web.setcookie('loggedin', user_data.username, expires="", domain=None, secure=False)
			raise web.seeother('/')
		else:
			raise web.

class Page:
	def GET(self, ID):
		return 

class Add_Argument:
	def POST(self):
		data = web.input()
		arguments = load_arguments() # REPLACE LATER
		next_ID = str(list(arguments)[-1][0]) + 1

		arguments[str(next_ID)] = {
			'text': data.text, 
			'mom': data.mom_ID, 
			'pro_sons':[], 
			'con_sons':[], 
			'supporters':[],
			'opponents':[],
			'author': web.cookies().get('loggedin')
		}

		if data.pro == True:
			arguments[str(data.mom_id)].pro_sons.append(next_ID)
		else:
			arguments[str(data.mom_id)].con_sons.append(next_ID)
		save_arguments(arguments)

class Get_Argument:
	def GET(self):
		ID = web.input().id
		arguments = load_arguments() # REPLACE LATER
		return json.dumps(arguments[str(ID)])

class Vote:
	def POST(self):
		user = web.cookies().get('loggedin')
		data = web.input()
		arguments = load_arguments()
		if data.pro == True:
			arguments[data.ID]['supporters'].append(user)
		else:
			arguments[data.ID]['opponents'].append(user)

if __name__ == "__main__":
	app.run()
