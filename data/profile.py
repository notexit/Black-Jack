import json, os

sav = os.path.abspath("profile.json")

def save(profile):
	f = open(sav, 'w')
	f.write(profile)
	f.close()

def load():
	try:
		with open(sav) as p:
			return json.load(p)
	except:
		pass

def create(name_profile, many_profile):
	profile = json.dumps({'name' : name_profile, 'many': many_profile}, sort_keys=True, indent = 4)
	save(profile)
