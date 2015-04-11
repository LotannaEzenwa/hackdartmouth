import sys
sys.path.insert(0, './python')
import web
import json
from bad_storage import *

urls = (
	'/', 'index',
	'/register', 'register',
	'/(\d+)', 'page',
	'/add_comment','add_comment',
	'/get_comment', 'get_comment'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		# return 'hello world'
		users = load_users() # REPLACE LATER
		if not web.cookies().get('loggedin') in users:
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
		save_users(users) # REPLACE LATER
		web.setcookie('loggedin', user_data.username, expires="", domain=None, secure=False)
		raise web.seeother('/')

class page:
	def GET(self, ID):
		return 'thanks for accessing argument' + str(ID)

class add_comment:
	def POST(self):
		data = web.input()
		comments = load_comments() # REPLACE LATER
		next_ID = str(list(comments)[-1][0]) + 1
		comments[str(next_ID)] = {'text': data.text, 'mom': data.mom_ID, 'pro_sons':[], 'con_sons':[], supporters}
		if data.pro == True:
			comments[str(data.mom_id)].pro_sons.append(next_ID)
		else:
			comments[str(data.mom_id)].con_sons.append(next_ID)
		save_comments(comments)

class get_comment:
	def GET(self):
		ID = web.input().id
		comments = load_comments() # REPLACE LATER
		return json.dumps(comments[str(ID)])

if __name__ == "__main__":
	app.run()