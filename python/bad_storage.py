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
		try:
			fl = open('./python/users.json','r')
			users = json.loads(fl.read())
			fl.close()
		except:
			open('./python/users.json','w').close()
			users = {}
	return users

def load_arguments():
	d = os.listdir('./python')
	if not 'arguments.json' in d:
		open('./python/arguments.json','w').close()
		arguments = {}
	else:
		try:
			fl = open('./python/arguments.json','r')
			arguments = json.loads(fl.read())
			fl.close()
		except:
			open('./python/arguments.json','w').close()
			arguments = {}
	return arguments

def load_philos():
	d = os.listdir('./python')
	if not 'philos.json' in d:
		open('./python/philos.json','w').close()
		philos = {}
	else:
		try:
			fl = open('./python/philos.json','r')
			philos = json.loads(fl.read())
			fl.close()
		except:
			open('./python/philos.json','w').close()
			philos = {}
	return philos

def save_users(users):
	out = open('./python/users.json', 'w')
	out.write(json.dumps(users))
	out.close()

def save_arguments(arguments):
	out = open('./python/arguments.json', 'w')
	out.write(json.dumps(arguments))
	out.close()

def save_philos(philos):
	out = open('./python/philos.json', 'w')
	out.write(json.dumps(philos))
	out.close()

''' END OF STUFF THAT SHOULD BE REPLACED '''