import web
import json
import os

''' Should be replaced eventually with a database solution that doesn't require opening a file
	and rewriting to it every time '''

def load_users():
	d = os.listdir('./python')
	print d
	if not 'users.json' in d:
		open('./python/users.json','w').close()
		users = {}
	else:
		users = json.loads(open('./python/users.json','r').read())
	return users

def load_comments():
	d = os.listdir('./python')
	if not 'comments.json' in d:
		open('./python/comments.json','w').close()
		comments = {}
	else:
		comments = json.loads(open('./python/comments.json','r').read())
	return comments

def save_users(users):
	out = open('./python/users.json', 'w')
	out.write(json.dumps(users))
	out.close()

def save_comments(comments):
	out = open('./python/users.json', 'w')
	out.write(json.dumps(users))
	out.close()

''' END OF STUFF THAT SHOULD BE REPLACED '''