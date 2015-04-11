import sys
# sys.path.insert(0, './python')
import web
# from bad_storage import *

urls = (
    '/(.*)', 'main'
    '/register(.*)', 'register'
)

app = web.application(urls, globals())

class register:        
	def POST(self, args):
		user_data = web.input()
		print user_data
		quit()
		users = load_users() # REPLACE LATER
		# users[user_data]

if __name__ == "__main__":
	app.run()